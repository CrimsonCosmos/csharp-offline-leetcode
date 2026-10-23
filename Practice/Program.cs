using System.Diagnostics;
using System.Reflection;
using System.Text;
using System.Text.Json;

// Generic test runner. Usage (normally via run.sh / run.ps1):
//   dotnet run -p:Problem=<folder name> -- <path to problem folder> [--unordered] [--all] [--stop]
//
// Loads <problem folder>/tests.json, builds the arguments from JSON using the parameter types of your
// Solution method, calls it, and compares the result with the expected value.

public static class Program {
    static readonly JsonSerializerOptions Opts = new JsonSerializerOptions {
        Converters = { new ListNodeConverter(), new TreeNodeConverter() },
    };

    const int MaxShownFailures = 3;
    const int TimeoutSeconds = 10;
    const int PerfTimeoutSeconds = 2;   // tests tagged "g":"perf" are large on purpose: an O(n^2) solution should fail them

    // --json: print one machine-readable result object (used by the web UI server) instead of text.
    // --limit=N: only run the first N tests.
    static bool json;
    static string Ns = "";
    static readonly StringWriter Cap = new StringWriter();
    static readonly StringBuilder UserOut = new StringBuilder();
    static readonly List<Dictionary<string, object>> Failures = new();
    static Dictionary<string, object> Timeout;
    static Dictionary<string, object> Summary = new();
    static readonly List<int> SkippedIdx = new();

    public static int Main(string[] args) {
        json = args.Contains("--json");
        TextWriter real = Console.Out;
        if (json) Console.SetOut(Cap);
        int code = Core(args);
        if (json) {
            Summary["code"] = code;
            Summary["skippedIdx"] = SkippedIdx;
            Summary["message"] = Cap.ToString().Trim();
            Summary["failures"] = Failures;
            if (Timeout != null) Summary["timeout"] = Timeout;
            Summary["stdout"] = UserOut.Length > 8000 ? UserOut.ToString(0, 8000) + "\n... (output truncated)" : UserOut.ToString();
            real.WriteLine(JsonSerializer.Serialize(Summary));
        }
        return code;
    }

    static int Core(string[] args) {
        var flags = new HashSet<string>(args.Where(a => a.StartsWith("--")));
        var pos = args.Where(a => !a.StartsWith("--")).ToList();
        if (pos.Count < 1) { Console.WriteLine("usage: dotnet run -p:Problem=<folder> -- <problem folder> [--unordered] [--all] [--stop]"); return 2; }
        int limit = int.MaxValue;
        foreach (var f in flags) if (f.StartsWith("--limit=")) limit = int.Parse(f.Substring(8));
        Ns = flags.Where(f => f.StartsWith("--ns=")).Select(f => f.Substring(5) + ".").FirstOrDefault() ?? "";   // used by the batch checker
        bool check = flags.Contains("--check");   // only verify that every test can be deserialized into the method's types
        bool unordered = flags.Contains("--unordered"), showAll = flags.Contains("--all"), stopAtFirst = flags.Contains("--stop");

        string dir = pos[0];
        string testsPath = Path.Combine(dir, "tests.json");
        string title = Path.GetFileName(dir.TrimEnd('/', '\\'));
        if (!File.Exists(testsPath)) {
            Console.WriteLine($"{title}: no tests.json in this folder (the test dataset doesn't cover this problem).");
            Console.WriteLine("Check your solution against the examples in README.md instead.");
            return 2;
        }

        using var doc = JsonDocument.Parse(File.ReadAllText(testsPath));
        var root = doc.RootElement;
        string methodName = root.GetProperty("method").GetString();
        bool inplace = root.GetProperty("inplace").GetBoolean();
        var paramNames = root.GetProperty("params").EnumerateArray().Select(p => p.GetString()).ToList();
        var tests = root.GetProperty("tests");

        if (root.TryGetProperty("design", out var dz) && dz.GetBoolean())
            return RunDesign(root, title, unordered, showAll, stopAtFirst, limit, check);

        var solType = Assembly.GetExecutingAssembly().GetType(Ns + "Solution");
        if (solType == null) { Console.WriteLine("Could not find `public class Solution`."); return 2; }
        var candidates = solType.GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.DeclaredOnly)
            .Where(m => string.Equals(m.Name, methodName, StringComparison.OrdinalIgnoreCase)).ToList();
        if (candidates.Count == 0) {
            Console.WriteLine($"Could not find a public method named {methodName} in class Solution. Keep the LeetCode method name.");
            return 2;
        }
        var method = candidates.FirstOrDefault(m => m.GetParameters().Length == paramNames.Count) ?? candidates[0];
        var ps = method.GetParameters();
        bool isVoid = method.ReturnType == typeof(void);
        int inplaceArg = root.TryGetProperty("inplaceArg", out var ia) ? ia.GetInt32() : -1;   // index of the argument that holds the result

        int pass = 0, fail = 0, orderOnly = 0, idx = 0, shown = 0, skipped = 0;
        string lastSkipReason = null;
        var sw = Stopwatch.StartNew();
        foreach (var t in tests.EnumerateArray()) {
            if (idx >= limit) break;
            idx++;
            var argEls = t.GetProperty("a").EnumerateArray().ToList();
            var expEl = t.GetProperty("e");

            object[] callArgs;
            try {
                callArgs = new object[ps.Length];
                for (int i = 0; i < ps.Length; i++) {
                    // A TreeNode parameter given as a bare number is a reference to the node with that value inside the
                    // tree passed in the first TreeNode parameter (e.g. p and q in Lowest Common Ancestor).
                    if (ps[i].ParameterType == typeof(TreeNode) && argEls[i].ValueKind == JsonValueKind.Number) continue;
                    callArgs[i] = argEls[i].Deserialize(ps[i].ParameterType, Opts);
                }
                for (int i = 0; i < ps.Length; i++) {
                    if (ps[i].ParameterType == typeof(TreeNode) && argEls[i].ValueKind == JsonValueKind.Number) {
                        var treeArg = callArgs.OfType<TreeNode>().FirstOrDefault();
                        callArgs[i] = FindNode(treeArg, argEls[i].GetInt32())
                            ?? throw new JsonException($"node {argEls[i].GetInt32()} is not in the tree");
                    }
                }
            } catch (Exception e) when (e is JsonException || e is NotSupportedException || e is InvalidOperationException) {
                // Either an unsupported parameter type, or (rarely) a generated test whose input isn't valid
                // for LeetCode's types, e.g. a float inside a TreeNode. Skip it and carry on.
                skipped++; SkippedIdx.Add(idx);
                lastSkipReason = e.Message.Split('\n')[0];
                continue;
            }

            if (check) {
                try {
                    var ct = isVoid ? (inplaceArg >= 0 ? ps[inplaceArg].ParameterType : null) : method.ReturnType;
                    if (ct != null && !(ct == typeof(TreeNode) && expEl.ValueKind == JsonValueKind.Number)) expEl.Deserialize(ct, Opts);
                    pass++;
                } catch (Exception e) when (e is JsonException || e is NotSupportedException || e is InvalidOperationException) {
                    skipped++; SkippedIdx.Add(idx); lastSkipReason = e.Message.Split('\n')[0];
                }
                continue;
            }
            bool perf = t.TryGetProperty("g", out var gTag) && gTag.ValueKind == JsonValueKind.String && gTag.GetString() == "perf";
            int limitSeconds = perf ? PerfTimeoutSeconds : TimeoutSeconds;
            var (result, err, timedOut) = Invoke(method, callArgs, limitSeconds);
            if (json) { if (UserOut.Length < 8000) UserOut.Append(Cap.ToString()); Cap.GetStringBuilder().Clear(); }
            if (timedOut) {
                Timeout = new() { ["i"] = idx, ["input"] = Show(paramNames, argEls), ["limit"] = limitSeconds };
                Summary["passed"] = pass; Summary["total"] = tests.GetArrayLength();
                Console.WriteLine($"TIMEOUT (> {limitSeconds}s) on test #{idx}: {Show(paramNames, argEls)}");
                Console.WriteLine($"{pass} passed before the timeout. Your solution is probably too slow or loops forever.");
                return 1;
            }
            if (err != null) {
                fail++;
                if (json && Failures.Count < 20) Failures.Add(new() { ["i"] = idx, ["input"] = Show(paramNames, argEls), ["error"] = $"{err.GetType().Name}: {err.Message}" });
                if (showAll || shown++ < MaxShownFailures)
                    Console.WriteLine($"FAIL #{idx}: threw {err.GetType().Name}: {err.Message}\n  input:    {Show(paramNames, argEls)}");
                if (stopAtFirst) break;
                continue;
            }

            // In-place problem without a stored final state (old tests.json): the dataset only asserts "== None".
            if (isVoid && inplaceArg < 0) { pass++; continue; }

            // In-place problems with "inplaceArg": compare the final state of that argument with `e`.
            var cmpType = isVoid ? ps[inplaceArg].ParameterType : method.ReturnType;
            var cmpValue = isVoid ? callArgs[inplaceArg] : result;
            JsonElement got, expected;
            try {
                if (cmpType == typeof(TreeNode) && expEl.ValueKind == JsonValueKind.Number) {
                    // node reference: compared by value
                    got = JsonSerializer.SerializeToElement(((TreeNode)cmpValue)?.val, typeof(int?), Opts);
                    expected = expEl;
                } else {
                    got = JsonSerializer.SerializeToElement(cmpValue, cmpType, Opts);
                    expected = JsonSerializer.SerializeToElement(expEl.Deserialize(cmpType, Opts), cmpType, Opts);
                }
            } catch (Exception e) when (e is JsonException || e is NotSupportedException || e is InvalidOperationException) {
                skipped++; SkippedIdx.Add(idx);
                lastSkipReason = e.Message.Split('\n')[0];
                continue;
            }

            bool ok = unordered ? Canon(got, true) == Canon(expected, true) : Eq(got, expected);
            if (ok) { pass++; continue; }

            fail++;
            bool onlyOrder = !unordered && Canon(got, true) == Canon(expected, true);
            if (onlyOrder) orderOnly++;
            if (json && Failures.Count < 20) Failures.Add(new() { ["i"] = idx, ["input"] = Show(paramNames, argEls), ["expected"] = Trunc(expected.GetRawText()), ["got"] = Trunc(got.GetRawText()), ["orderOnly"] = onlyOrder });
            if (showAll || shown++ < MaxShownFailures) {
                Console.WriteLine($"FAIL #{idx}{(onlyOrder ? " (same elements, different order)" : "")}");
                Console.WriteLine($"  input:    {Show(paramNames, argEls)}");
                Console.WriteLine($"  expected: {Trunc(expected.GetRawText())}");
                Console.WriteLine($"  got:      {Trunc(got.GetRawText())}");
            }
            if (stopAtFirst) break;
        }
        sw.Stop();

        int total = pass + fail;
        Summary["passed"] = pass; Summary["total"] = total; Summary["skipped"] = skipped; Summary["ms"] = sw.ElapsedMilliseconds;
        Summary["inplace"] = isVoid && inplace && inplaceArg < 0; Summary["orderOnly"] = orderOnly; Summary["failCount"] = fail;
        if (total == 0 && skipped > 0) {
            Console.WriteLine($"{title}: the runner can't build or compare this method's types from JSON ({lastSkipReason}).");
            Console.WriteLine("Check your solution against the examples in README.md instead.");
            return 2;
        }
        string tag = fail == 0 ? "PASS" : "FAIL";
        Console.WriteLine($"{tag} {title}: {pass}/{total} tests passed ({sw.ElapsedMilliseconds} ms)");
        if (skipped > 0)
            Console.WriteLine($"Note: {skipped} generated test(s) skipped because their input isn't valid for LeetCode's types (e.g. a decimal inside a tree).");
        if (isVoid && inplace && inplaceArg < 0)
            Console.WriteLine("Note: this is an in-place problem. The dataset's tests only check that your code runs without throwing, not the modified result. Verify against the README examples.");
        if (orderOnly > 0)
            Console.WriteLine($"Note: {orderOnly} failure(s) have the right elements in a different order. If this problem accepts any order, re-run with --unordered.");
        if (fail > shown && !showAll) Console.WriteLine($"(showing first {MaxShownFailures} failures; use --all to see every one)");
        return fail == 0 ? 0 : 1;
    }

    static TreeNode FindNode(TreeNode root, int val) {
        var q = new Queue<TreeNode>();
        if (root != null) q.Enqueue(root);
        while (q.Count > 0) {
            var n = q.Dequeue();
            if (n.val == val) return n;
            if (n.left != null) q.Enqueue(n.left);
            if (n.right != null) q.Enqueue(n.right);
        }
        return null;
    }

    static (object result, Exception err, bool timedOut) Invoke(MethodInfo m, object[] callArgs, int seconds) {
        object result = null; Exception err = null;
        var th = new Thread(() => {
            try { result = m.Invoke(Activator.CreateInstance(m.DeclaringType), callArgs); }
            catch (TargetInvocationException e) { err = e.InnerException ?? e; }
            catch (Exception e) { err = e; }
        }, 256 * 1024 * 1024);   // big stack so deep recursion behaves like LeetCode
        th.IsBackground = true;
        th.Start();
        if (!th.Join(TimeSpan.FromSeconds(seconds))) return (null, null, true);
        return (result, err, false);
    }

    // Design problems ("design": true in tests.json): each test is a sequence of operations on one object, like LeetCode's
    // "Input: ["Cls","op1",...] [[ctorArgs],[args1],...]  Output: [null, r1, ...]".
    static int RunDesign(JsonElement root, string title, bool unordered, bool showAll, bool stopAtFirst, int limit, bool check) {
        string cls = root.GetProperty("class").GetString();
        var type = Assembly.GetExecutingAssembly().GetType(Ns + cls);
        if (type == null) { Console.WriteLine($"Could not find `public class {cls}`. Keep the LeetCode class name."); return 2; }
        var tests = root.GetProperty("tests");
        int pass = 0, fail = 0, idx = 0, shown = 0, skipped = 0;
        var sw = Stopwatch.StartNew();
        foreach (var t in tests.EnumerateArray()) {
            if (idx >= limit) break;
            idx++;
            var ops = t.GetProperty("ops").EnumerateArray().Select(o => o.GetString()).ToList();
            var args = t.GetProperty("a").EnumerateArray().ToList();
            var exps = t.GetProperty("e").EnumerateArray().ToList();
            if (check) { pass++; continue; }

            string failure = null;
            var th = new Thread(() => {
                object inst = null;
                for (int k = 0; k < ops.Count && failure == null; k++) {
                    var argEls = args[k].EnumerateArray().ToList();
                    string call = $"{ops[k]}({string.Join(", ", argEls.Select(a => Trunc(a.GetRawText())))})";
                    try {
                        object res; Type rt;
                        if (k == 0) {
                            var ctor = type.GetConstructors().FirstOrDefault(c => c.GetParameters().Length == argEls.Count)
                                ?? throw new MissingMethodException($"no public constructor with {argEls.Count} parameter(s)");
                            inst = ctor.Invoke(BuildArgs(ctor.GetParameters(), argEls));
                            res = null; rt = typeof(void);
                        } else {
                            var m = type.GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.DeclaredOnly)
                                .FirstOrDefault(x => string.Equals(x.Name, ops[k], StringComparison.OrdinalIgnoreCase) && x.GetParameters().Length == argEls.Count)
                                ?? throw new MissingMethodException($"no public method {ops[k]} with {argEls.Count} parameter(s)");
                            res = m.Invoke(inst, BuildArgs(m.GetParameters(), argEls)); rt = m.ReturnType;
                        }
                        var expEl = exps[k];
                        if (rt == typeof(void)) continue;   // LeetCode prints null for void methods
                        var got = JsonSerializer.SerializeToElement(res, rt, Opts);
                        var expected = JsonSerializer.SerializeToElement(expEl.Deserialize(rt, Opts), rt, Opts);
                        bool ok = unordered ? Canon(got, true) == Canon(expected, true) : Eq(got, expected);
                        if (!ok) failure = $"step {k + 1}: {call}\n  expected: {Trunc(expected.GetRawText())}\n  got:      {Trunc(got.GetRawText())}"
                            + (Failures.Count < 20 ? "" : "");
                    } catch (TargetInvocationException e) {
                        failure = $"step {k + 1}: {call} threw {e.InnerException?.GetType().Name}: {e.InnerException?.Message}";
                    } catch (Exception e) {
                        failure = $"step {k + 1}: {call}: {e.Message}";
                    }
                }
            }, 256 * 1024 * 1024);
            th.IsBackground = true; th.Start();
            if (!th.Join(TimeSpan.FromSeconds(TimeoutSeconds))) {
                Timeout = new() { ["i"] = idx, ["input"] = "operations: " + string.Join(", ", ops.Take(12)) };
                Summary["passed"] = pass; Summary["total"] = tests.GetArrayLength();
                Console.WriteLine($"TIMEOUT (> {TimeoutSeconds}s) on test #{idx}");
                return 1;
            }
            if (json) { if (UserOut.Length < 8000) UserOut.Append(Cap.ToString()); Cap.GetStringBuilder().Clear(); }
            if (failure == null) { pass++; continue; }
            fail++;
            var headline = failure.Split('\n')[0];
            if (json && Failures.Count < 20) {
                var parts = failure.Split('\n');
                var f = new Dictionary<string, object> { ["i"] = idx, ["input"] = "operations: " + string.Join(", ", ops.Take(8)) + (ops.Count > 8 ? ", ..." : "") };
                if (parts.Length >= 3) { f["expected"] = parts[1].Replace("  expected: ", ""); f["got"] = parts[2].Replace("  got:      ", ""); f["step"] = headline; }
                else f["error"] = headline;
                Failures.Add(f);
            }
            if (showAll || shown++ < MaxShownFailures) Console.WriteLine($"FAIL #{idx}: {failure}");
            if (stopAtFirst) break;
        }
        sw.Stop();
        Summary["passed"] = pass; Summary["total"] = pass + fail; Summary["skipped"] = skipped; Summary["ms"] = sw.ElapsedMilliseconds;
        Summary["inplace"] = false; Summary["orderOnly"] = 0; Summary["failCount"] = fail;
        Console.WriteLine($"{(fail == 0 ? "PASS" : "FAIL")} {title}: {pass}/{pass + fail} tests passed ({sw.ElapsedMilliseconds} ms)");
        return fail == 0 ? 0 : 1;
    }

    static object[] BuildArgs(ParameterInfo[] ps, List<JsonElement> els) {
        var a = new object[ps.Length];
        for (int i = 0; i < ps.Length; i++) a[i] = els[i].Deserialize(ps[i].ParameterType, Opts);
        return a;
    }

    static string Show(List<string> names, List<JsonElement> args) {
        var sb = new StringBuilder();
        for (int i = 0; i < args.Count; i++) {
            if (i > 0) sb.Append(", ");
            sb.Append(i < names.Count ? names[i] : $"arg{i}").Append(" = ").Append(Trunc(args[i].GetRawText()));
        }
        return sb.ToString();
    }

    static string Trunc(string s) => s.Length <= 220 ? s : s.Substring(0, 220) + $"... ({s.Length} chars)";

    static bool Eq(JsonElement a, JsonElement b) {
        if (a.ValueKind != b.ValueKind) return false;
        switch (a.ValueKind) {
            case JsonValueKind.Number: {
                string ra = a.GetRawText(), rb = b.GetRawText();
                if (ra == rb) return true;
                bool fuzzy = ra.IndexOfAny(new[] { '.', 'e', 'E' }) >= 0 || rb.IndexOfAny(new[] { '.', 'e', 'E' }) >= 0;
                if (!fuzzy) return false;
                double x = a.GetDouble(), y = b.GetDouble();
                return Math.Abs(x - y) <= 1e-5 * Math.Max(1.0, Math.Abs(y));   // LeetCode-style tolerance
            }
            case JsonValueKind.String: return a.GetString() == b.GetString();
            case JsonValueKind.Array: {
                var la = a.EnumerateArray().ToList(); var lb = b.EnumerateArray().ToList();
                if (la.Count != lb.Count) return false;
                for (int i = 0; i < la.Count; i++) if (!Eq(la[i], lb[i])) return false;
                return true;
            }
            case JsonValueKind.Object: {
                var pa = a.EnumerateObject().ToDictionary(p => p.Name, p => p.Value);
                var pb = b.EnumerateObject().ToDictionary(p => p.Name, p => p.Value);
                if (pa.Count != pb.Count) return false;
                foreach (var kv in pa) if (!pb.TryGetValue(kv.Key, out var o) || !Eq(kv.Value, o)) return false;
                return true;
            }
            default: return true;   // true/true, false/false, null/null
        }
    }

    // Canonical text; with sortArrays=true the order of every array (at every depth) is ignored.
    static string Canon(JsonElement e, bool sortArrays) {
        switch (e.ValueKind) {
            case JsonValueKind.Array: {
                var parts = e.EnumerateArray().Select(x => Canon(x, sortArrays)).ToList();
                if (sortArrays) parts.Sort(StringComparer.Ordinal);
                return "[" + string.Join(",", parts) + "]";
            }
            case JsonValueKind.Object:
                return "{" + string.Join(",", e.EnumerateObject().OrderBy(p => p.Name, StringComparer.Ordinal)
                    .Select(p => JsonSerializer.Serialize(p.Name) + ":" + Canon(p.Value, sortArrays))) + "}";
            case JsonValueKind.Number: {
                string raw = e.GetRawText();
                return raw.IndexOfAny(new[] { '.', 'e', 'E' }) >= 0 ? Math.Round(e.GetDouble(), 5).ToString("R") : raw;
            }
            default: return e.GetRawText();
        }
    }
}
