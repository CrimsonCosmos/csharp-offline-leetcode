using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.RegularExpressions;
using Microsoft.Extensions.FileProviders;

// Local LeetCode-style web UI for the offline C# practice pack.
//   dotnet run --project Server            (normally started by the "Start LeetCode" launcher)
// Options: --no-browser, --port=N

var root = FindRoot();
var dataDir = Path.Combine(root, "userdata");
Directory.CreateDirectory(dataDir);
var portFile = Path.Combine(dataDir, "server.url");
bool openBrowser = !args.Contains("--no-browser");

// If a server from an earlier double-click is still running, just open its page.
if (File.Exists(portFile)) {
    var old = File.ReadAllText(portFile).Trim();
    if (await Ping(old)) {
        Console.WriteLine($"LeetCode is already running at {old}");
        if (openBrowser) OpenUrl(old);
        return;
    }
}

int port = 0;
var portArg = args.FirstOrDefault(a => a.StartsWith("--port="));
if (portArg != null) port = int.Parse(portArg.Substring(7));
else foreach (var p in new[] { 5180, 5181, 5182 }) if (PortFree(p)) { port = p; break; }

var builder = WebApplication.CreateBuilder(new WebApplicationOptions { Args = args, ContentRootPath = root });
builder.Logging.ClearProviders();
builder.WebHost.UseUrls($"http://127.0.0.1:{port}");
builder.Services.ConfigureHttpJsonOptions(o => o.SerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase);
var app = builder.Build();

// Show unexpected server errors in the console and return their message to the page instead of a bare "500".
app.Use(async (ctx, next) => {
    try { await next(); }
    catch (Exception e) {
        Console.WriteLine($"\n[error] {ctx.Request.Method} {ctx.Request.Path}\n{e}\n");
        if (!ctx.Response.HasStarted) {
            ctx.Response.StatusCode = 500;
            ctx.Response.ContentType = "text/plain";
            await ctx.Response.WriteAsync($"{e.GetType().Name}: {e.Message}");
        }
    }
});

var store = new Store(root, dataDir);
var sync = new CloudSync(dataDir);

var web = Path.Combine(root, "web");
var files = new PhysicalFileProvider(web);
app.UseDefaultFiles(new DefaultFilesOptions { FileProvider = files });
app.UseStaticFiles(new StaticFileOptions { FileProvider = files });

app.MapGet("/api/ping", () => Results.Text("leetcode-offline"));

app.MapGet("/api/problems", () => store.List());
app.MapGet("/api/problems/{folder}", (string folder) => store.Get(folder) is { } p ? Results.Ok(p) : Results.NotFound());
app.MapGet("/api/problems/{folder}/editorial", (string folder) => {
    var f = Path.Combine(store.ProblemDir(folder) ?? "", "EDITORIAL_SPOILERS.md");
    return File.Exists(f) ? Results.Text(File.ReadAllText(f), "text/markdown") : Results.NotFound();
});
app.MapPut("/api/problems/{folder}/code", async (string folder, HttpRequest req) => {
    if (store.ProblemDir(folder) == null) return Results.NotFound();
    store.SaveCode(folder, await new StreamReader(req.Body).ReadToEndAsync());
    return Results.NoContent();
});
app.MapDelete("/api/problems/{folder}/code", (string folder) => { store.ResetCode(folder); return Results.NoContent(); });
app.MapPost("/api/problems/{folder}/mark", (string folder, JsonElement body) => {
    store.Mark(folder, body.GetProperty("solved").GetBoolean());
    return Results.NoContent();
});
app.MapGet("/api/sync", () => sync.Status());
app.MapPost("/api/sync/setup", async (JsonElement body) => Results.Json(await sync.Setup(body.GetProperty("remote").GetString())));
app.MapPost("/api/sync/now", () => { sync.Trigger("Manual backup"); return Results.Json(sync.Status()); });
app.MapDelete("/api/sync", () => { sync.Disable(); return Results.NoContent(); });
app.MapPost("/api/problems/{folder}/run", async (string folder, JsonElement body) => {
    if (store.ProblemDir(folder) == null) return Results.NotFound();
    var code = body.GetProperty("code").GetString();
    var submit = body.TryGetProperty("submit", out var s) && s.GetBoolean();
    var unordered = body.TryGetProperty("unordered", out var u) && u.GetBoolean();
    store.SaveCode(folder, code);
    var result = await Runner.Run(root, dataDir, folder, code, submit, unordered);
    if (submit) {
        store.RecordSubmission(folder, code, result);
        if (result["status"]?.GetValue<string>() == "accepted") sync.Trigger($"Solved {folder}");   // back up in the background
    }
    return Results.Json(result);
});

var lifetime = app.Lifetime;
lifetime.ApplicationStopping.Register(() => { try { File.Delete(portFile); } catch { } });
await app.StartAsync();
var url = app.Urls.First().Replace("127.0.0.1", "localhost");
var bound = app.Urls.First();
File.WriteAllText(portFile, bound);
Console.WriteLine();
Console.WriteLine("  C# LeetCode (offline)");
Console.WriteLine($"  Running at {url}");
Console.WriteLine("  Keep this window open while you practice. Close it (or press Ctrl+C) to stop.");
Console.WriteLine();
if (openBrowser) OpenUrl(url);
await app.WaitForShutdownAsync();

// ---------------------------------------------------------------------------------------------

static string FindRoot() {
    foreach (var start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory }) {
        var d = new DirectoryInfo(start);
        while (d != null) {
            if (Directory.Exists(Path.Combine(d.FullName, "problems")) && Directory.Exists(Path.Combine(d.FullName, "Practice")))
                return d.FullName;
            d = d.Parent;
        }
    }
    throw new Exception("Could not find the project root (a folder containing 'problems' and 'Practice').");
}

static bool PortFree(int p) {
    try { var l = new TcpListener(IPAddress.Loopback, p); l.Start(); l.Stop(); return true; } catch { return false; }
}

static async Task<bool> Ping(string url) {
    try {
        using var c = new HttpClient { Timeout = TimeSpan.FromSeconds(1.5) };
        return (await c.GetStringAsync(url.TrimEnd('/') + "/api/ping")) == "leetcode-offline";
    } catch { return false; }
}

static void OpenUrl(string url) {
    try {
        if (OperatingSystem.IsWindows()) Process.Start(new ProcessStartInfo(url) { UseShellExecute = true });
        else if (OperatingSystem.IsMacOS()) Process.Start("open", url);
        else Process.Start("xdg-open", url);
    } catch (Exception e) {
        Console.WriteLine($"  (Could not open a browser automatically: {e.Message}. Open {url} yourself.)");
    }
}

// ---------------------------------------------------------------------------------------------

class Store {
    readonly string root, data, codeDir, progressFile;
    readonly object gate = new();
    readonly List<ProblemInfo> problems = new();
    readonly Dictionary<string, ProblemInfo> byFolder = new();
    Dictionary<string, Progress> progress = new();
    static readonly JsonSerializerOptions Json = new() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase, WriteIndented = true };

    public Store(string root, string data) {
        this.root = root; this.data = data;
        codeDir = Path.Combine(data, "code"); Directory.CreateDirectory(codeDir);
        progressFile = Path.Combine(data, "progress.json");
        if (File.Exists(progressFile)) {
            try { progress = JsonSerializer.Deserialize<Dictionary<string, Progress>>(File.ReadAllText(progressFile), Json) ?? new(); } catch { }
        }
        foreach (var line in File.ReadLines(Path.Combine(root, "INDEX.md"))) {
            var c = line.Split('|').Select(x => x.Trim()).ToArray();   // "", #, title, topics, tests, folder, ""
            if (c.Length < 7 || !int.TryParse(c[1], out var id)) continue;
            var p = new ProblemInfo {
                Id = id, Title = c[2], Folder = c[5],
                Topics = c[3].Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries),
                Tests = int.TryParse(c[4], out var n) ? n : 0,
            };
            problems.Add(p); byFolder[p.Folder] = p;
        }
    }

    public string ProblemDir(string folder) =>
        byFolder.ContainsKey(folder) ? Path.Combine(root, "problems", folder) : null;

    string Status(string folder) => progress.TryGetValue(folder, out var p) ? p.Status : null;

    public object List() { lock (gate) return problems.Select(p => new {
        p.Id, p.Title, p.Folder, p.Topics, p.Tests, Difficulty = "Medium", Status = Status(p.Folder),
    }).ToList(); }

    public object Get(string folder) {
        var dir = ProblemDir(folder);
        if (dir == null) return null;
        var p = byFolder[folder];
        var readme = File.ReadAllText(Path.Combine(dir, "README.md"));
        var starter = File.ReadAllText(Path.Combine(dir, "Solution.cs"));
        var codeFile = Path.Combine(codeDir, folder + ".cs");
        var unordered = false; var examplesOnly = false;
        var testsFile = Path.Combine(dir, "tests.json");
        if (File.Exists(testsFile)) {
            using var td = JsonDocument.Parse(File.ReadAllText(testsFile));
            unordered = td.RootElement.TryGetProperty("unordered", out var u) && u.GetBoolean();
            examplesOnly = td.RootElement.TryGetProperty("examplesOnly", out var eo) && eo.GetBoolean();
        }
        lock (gate) {
            progress.TryGetValue(folder, out var pr);
            return new {
                p.Id, p.Title, p.Folder, p.Topics, p.Tests, Difficulty = "Medium",
                Link = Regex.Match(readme, @"\*\*Link \(online only\):\*\*\s*(\S+)").Groups[1].Value,
                Readme = readme, Starter = starter,
                Code = File.Exists(codeFile) ? File.ReadAllText(codeFile) : null,
                Unordered = unordered, ExamplesOnly = examplesOnly,
                HasEditorial = File.Exists(Path.Combine(dir, "EDITORIAL_SPOILERS.md")),
                Status = pr?.Status, Submissions = pr?.Submissions ?? new List<Submission>(),
            };
        }
    }

    public void SaveCode(string folder, string code) => File.WriteAllText(Path.Combine(codeDir, folder + ".cs"), code);
    public void ResetCode(string folder) { var f = Path.Combine(codeDir, folder + ".cs"); if (File.Exists(f)) File.Delete(f); }

    public void Mark(string folder, bool solved) { lock (gate) {
        var p = Prog(folder);
        p.Status = solved ? "solved" : (p.Submissions.Count > 0 ? "attempted" : null);
        Persist();
    } }

    public void RecordSubmission(string folder, string code, JsonNode result) { lock (gate) {
        var p = Prog(folder);
        var status = result["status"]?.GetValue<string>() ?? "error";
        p.Submissions.Insert(0, new Submission {
            Time = DateTime.UtcNow, Status = status, Passed = result["passed"]?.GetValue<int>() ?? 0,
            Total = result["total"]?.GetValue<int>() ?? 0, Ms = result["ms"]?.GetValue<long>() ?? 0, Code = code,
        });
        if (p.Submissions.Count > 30) p.Submissions.RemoveRange(30, p.Submissions.Count - 30);
        if (status == "accepted") p.Status = "solved";
        else if (p.Status != "solved") p.Status = "attempted";
        Persist();
    } }

    Progress Prog(string folder) {
        if (!progress.TryGetValue(folder, out var p)) progress[folder] = p = new Progress();
        return p;
    }
    void Persist() => File.WriteAllText(progressFile, JsonSerializer.Serialize(progress, Json));
}

class ProblemInfo { public int Id; public string Title, Folder; public string[] Topics; public int Tests; }
class Progress { public string Status { get; set; } public List<Submission> Submissions { get; set; } = new(); }
class Submission { public DateTime Time { get; set; } public string Status { get; set; } public int Passed { get; set; } public int Total { get; set; } public long Ms { get; set; } public string Code { get; set; } }


// ---------------------------------------------------------------------------------------------

/// <summary>
/// Backs the userdata folder up to a private Git repository (free on GitHub/GitLab/Bitbucket) after every accepted
/// submission. userdata becomes its own git repo; the remote is set once from the UI. Uses the machine's existing git
/// credentials, never blocks the app, and never deletes local data (on conflicts the local copy wins).
/// </summary>
class CloudSync {
    readonly string dir;
    readonly SemaphoreSlim gate = new(1);
    volatile string state = "idle";            // idle | running | ok | error
    volatile string message = "";
    DateTime? last;
    int pending;

    public CloudSync(string dir) { this.dir = dir; }

    bool IsRepo => Directory.Exists(Path.Combine(dir, ".git"));

    string Remote() {
        if (!IsRepo) return null;
        var r = Git("remote get-url origin").Result;
        return r.code == 0 ? r.output.Trim() : null;
    }
    bool HasRemote() => Remote() != null;

    public object Status() {
        var remote = Remote();
        return new { gitAvailable = GitAvailable(), enabled = remote != null, remote, state, message, last };
    }

    static bool GitAvailable() {
        try { using var p = Process.Start(new ProcessStartInfo("git", "--version") { RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false }); p.WaitForExit(5000); return p.ExitCode == 0; }
        catch { return false; }
    }

    public void Disable() {
        if (IsRepo) Git("remote remove origin").Wait();
        state = "idle"; message = "";
    }

    public async Task<object> Setup(string remote) {
        remote = (remote ?? "").Trim();
        if (remote.Length == 0) return new { ok = false, error = "Paste the URL of an empty private repository." };
        if (!GitAvailable()) return new { ok = false, error = "Git is not installed. Install it from https://git-scm.com and try again." };
        await gate.WaitAsync();
        try {
            Directory.CreateDirectory(dir);
            if (!IsRepo) { await Git("init"); await Git("checkout -B main"); }
            File.WriteAllText(Path.Combine(dir, ".gitignore"), "build/\nserver.url\n*.tmp\n");
            await Git("remote remove origin");
            var add = await Git("remote add origin", remote);
            if (add.code != 0) return new { ok = false, error = add.output.Trim() };
            var probe = await Git("ls-remote --heads origin", timeoutSec: 60);
            if (probe.code != 0) return new { ok = false, error = "Could not reach the repository. Check the URL, and that git is signed in (try `git ls-remote " + remote + "` in a terminal).\n" + Tail(probe.output) };
            // Remote already has backups (e.g. a new computer): merge them in; local files win on conflicts.
            if (probe.output.Contains("refs/heads/main")) {
                await Git("fetch origin main", timeoutSec: 120);
                await Commit("Backup before merge");
                var m = await Git("merge origin/main --allow-unrelated-histories -X ours --no-edit -m", "Merge cloud backup");
                if (m.code != 0) { await Git("merge --abort"); return new { ok = false, error = "Could not merge the cloud backup:\n" + Tail(m.output) }; }
            }
        } finally { gate.Release(); }
        Trigger("Set up cloud backup");
        return new { ok = true };
    }

    /// <summary>Queue a backup; returns immediately. Bursts are coalesced into one more run.</summary>
    public void Trigger(string reason) {
        if (!HasRemote()) return;
        Interlocked.Exchange(ref pending, 1);
        state = "running"; message = "Backing up...";
        _ = Task.Run(async () => {
            await gate.WaitAsync();
            try {
                while (Interlocked.Exchange(ref pending, 0) == 1) await Run(reason);
            } finally { gate.Release(); }
        });
    }

    async Task Run(string reason) {
        try {
            await Commit(reason);
            var push = await Git("push -u origin main", timeoutSec: 120);
            if (push.code != 0) {
                // remote moved on (another computer): merge, local wins, push again
                await Git("fetch origin main", timeoutSec: 120);
                var m = await Git("merge origin/main --allow-unrelated-histories -X ours --no-edit -m", "Merge cloud backup");
                if (m.code != 0) await Git("merge --abort");
                push = await Git("push -u origin main", timeoutSec: 120);
            }
            if (push.code == 0) { state = "ok"; message = "Backed up to the cloud"; last = DateTime.UtcNow; }
            else { state = "error"; message = "Backup failed: " + Tail(push.output); }
        } catch (Exception e) { state = "error"; message = "Backup failed: " + e.Message; }
    }

    async Task Commit(string msg) {
        await Git("add -A");
        var diff = await Git("diff --cached --quiet");
        if (diff.code != 0) await Git("commit -m", msg);
    }

    static string Tail(string s) { s = s.Trim(); return s.Length > 400 ? s[^400..] : s; }

    async Task<(int code, string output)> Git(string args, string lastArg = null, int timeoutSec = 30) {
        var psi = new ProcessStartInfo("git") { WorkingDirectory = dir, RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false };
        foreach (var a in new[] { "-c", "user.name=C# LeetCode Backup", "-c", "user.email=backup@localhost", "-c", "core.autocrlf=false" }) psi.ArgumentList.Add(a);
        foreach (var a in args.Split(' ')) psi.ArgumentList.Add(a);
        if (lastArg != null) psi.ArgumentList.Add(lastArg);      // message / URL passed as one argument
        psi.Environment["GIT_TERMINAL_PROMPT"] = "0";             // fail instead of hanging on a password prompt
        using var p = Process.Start(psi);
        var o = p.StandardOutput.ReadToEndAsync(); var e = p.StandardError.ReadToEndAsync();
        using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(timeoutSec));
        try { await p.WaitForExitAsync(cts.Token); }
        catch (OperationCanceledException) { try { p.Kill(true); } catch { } return (-1, "git timed out"); }
        return (p.ExitCode, (await o) + (await e));
    }
}

// ---------------------------------------------------------------------------------------------

static class Runner {
    static readonly SemaphoreSlim Slots = new(2);
    static readonly Regex ErrorLine = new(@"Solution\.cs\((\d+),(\d+)\):\s*error\s+(\w+):\s*(.*?)(\s*\[[^\]]*\])?$", RegexOptions.Compiled);

    static readonly System.Collections.Concurrent.ConcurrentDictionary<string, SemaphoreSlim> FolderLocks = new();

    public static async Task<JsonNode> Run(string root, string data, string folder, string code, bool submit, bool unordered) {
        var folderLock = FolderLocks.GetOrAdd(folder, _ => new SemaphoreSlim(1));
        await folderLock.WaitAsync();       // two runs of the same problem would fight over its build folder
        await Slots.WaitAsync();
        try {
            var build = Path.Combine(data, "build", folder);
            Directory.CreateDirectory(build);
            File.WriteAllText(Path.Combine(build, "Solution.cs"), code);
            var pdir = Path.Combine(root, "Practice");
            File.WriteAllText(Path.Combine(build, "Practice.csproj"), $"""
                <Project Sdk="Microsoft.NET.Sdk">
                  <PropertyGroup>
                    <OutputType>Exe</OutputType>
                    <TargetFramework>net8.0</TargetFramework>
                    <RollForward>Major</RollForward>
                    <ImplicitUsings>enable</ImplicitUsings>
                    <Nullable>disable</Nullable>
                    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
                    <InvariantGlobalization>true</InvariantGlobalization>
                    <SatelliteResourceLanguages>en</SatelliteResourceLanguages>
                    <NoWarn>CS8632;CS0168;CS0219;CS8981</NoWarn>
                    <TieredPGO>false</TieredPGO>
                  </PropertyGroup>
                  <ItemGroup>
                    <Compile Include="{Path.Combine(pdir, "Program.cs")}" />
                    <Compile Include="{Path.Combine(pdir, "Helpers.cs")}" />
                    <Compile Include="Solution.cs" />
                  </ItemGroup>
                </Project>
                """);

            var b = await Exec("dotnet", new[] { "build", "-c", "Release", "--nologo", "-v", "q", "-clp:NoSummary" }, build, 120);
            var errors = new List<object>();
            var seen = new HashSet<string>();
            foreach (var line in (b.Out + "\n" + b.Err).Split('\n')) {
                var m = ErrorLine.Match(line.Trim());
                if (m.Success && seen.Add(m.Value))
                    errors.Add(new { line = int.Parse(m.Groups[1].Value), col = int.Parse(m.Groups[2].Value), code = m.Groups[3].Value, message = m.Groups[4].Value });
            }
            if (b.ExitCode != 0) {
                return new JsonObject {
                    ["status"] = "compile_error",
                    ["errors"] = JsonSerializer.SerializeToNode(errors),
                    ["raw"] = errors.Count == 0 ? (b.Out + b.Err).Trim() : null,
                };
            }

            var dll = Path.Combine(build, "bin", "Release", "net8.0", "Practice.dll");
            var runArgs = new List<string> { "exec", dll, Path.Combine(root, "problems", folder), "--json" };
            if (!submit) runArgs.Add("--limit=10");
            if (unordered) runArgs.Add("--unordered");
            var r = await Exec("dotnet", runArgs, build, 120);
            JsonNode res;
            try { res = JsonNode.Parse(r.Out.Trim().Split('\n').Last(l => l.TrimStart().StartsWith("{"))); }
            catch { return new JsonObject { ["status"] = "runtime_error", ["raw"] = (r.Out + r.Err).Trim() }; }

            int code_ = res["code"]?.GetValue<int>() ?? 1;
            int failCount = res["failCount"]?.GetValue<int>() ?? 0;
            string status =
                res["timeout"] != null ? "timeout" :
                code_ == 2 ? "no_tests" :
                failCount == 0 ? "accepted" :
                (res["failures"] is JsonArray fa && fa.Any(f => f?["error"] != null) && fa.All(f => f?["error"] != null) ? "runtime_error" : "wrong_answer");
            res["status"] = status;
            res["submit"] = submit;
            return res;
        } finally { Slots.Release(); folderLock.Release(); }
    }

    record Proc(int ExitCode, string Out, string Err);

    static async Task<Proc> Exec(string exe, IEnumerable<string> args, string cwd, int timeoutSec) {
        var psi = new ProcessStartInfo(exe) { WorkingDirectory = cwd, RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false };
        foreach (var a in args) psi.ArgumentList.Add(a);
        psi.Environment["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1";
        psi.Environment["DOTNET_NOLOGO"] = "1";
        psi.Environment["DOTNET_SKIP_FIRST_TIME_EXPERIENCE"] = "1";
        using var p = Process.Start(psi);
        var o = p.StandardOutput.ReadToEndAsync();
        var e = p.StandardError.ReadToEndAsync();
        using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(timeoutSec));
        try { await p.WaitForExitAsync(cts.Token); }
        catch (OperationCanceledException) { try { p.Kill(true); } catch { } return new Proc(-1, await o, "Timed out.\n" + await e); }
        return new Proc(p.ExitCode, await o, await e);
    }
}
