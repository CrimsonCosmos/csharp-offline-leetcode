# C# LeetCode (offline)

A LeetCode-style web UI for practicing 1,413 Medium problems in C#, fully offline. Editor, problem statements, Run/Submit against ~121,000 test cases, progress tracking and editorials all run on your machine.

## Start it

Requirements: the **.NET 8 SDK or newer** (the launcher offers to install it if it's missing).

| OS | Double-click |
|---|---|
| Windows | `Start LeetCode.bat` |
| macOS | `Start LeetCode.command` (first time: right-click → Open) |
| Linux | `start-leetcode.sh` |

It starts the local server on a free port (5180 by default) and opens your default browser at the right URL. Keep the console window open while practicing; close it to stop. Double-clicking again while it's running just reopens the page.

**Desktop shortcut:** run `Create Desktop Shortcut.bat` (Windows) or `create-desktop-shortcut.sh` (macOS/Linux) once. The shortcut points at this folder, so don't move the folder afterwards (or re-run it).

## Using it

- **Problem list:** search, filter by topic/status, pick a random problem.
- **Run** (`Ctrl+'`) checks the first 10 test cases; **Submit** (`Ctrl+Enter`) checks all of them. Compile errors show as squiggles in the editor; failures show input / output / expected; `Console.WriteLine` output appears under Stdout.
- Code autosaves to `userdata/code/`; progress and submission history live in `userdata/progress.json` (git-ignored). Delete `userdata/` to start fresh.
- Tick **ignore result order** for problems that accept answers in any order.
- Problems without a test suite can be marked solved by hand. Problems tagged *examples only* use the statement's examples as tests; design problems (e.g. LRU Cache) run the example operation sequences.
- Known gaps: 10 problems that need a `Node` class (n-ary trees, quad trees, random-pointer lists, ...) and a few random/interactive problems have no tests and may not compile in the runner.

The tests started as LLM-generated cases from the open LeetCodeDataset, not LeetCode's hidden tests. They have since been audited (invalid cases removed, large and generated cases added, in-place and design problems verified); see [TEST_QUALITY.md](TEST_QUALITY.md) for what was done and what it does and does not prove, and [PRACTICE_PACK_README.md](PRACTICE_PACK_README.md) for the original caveats. The original CLI (`./run.sh 2`, `.\run.ps1 2`) still works.

## Layout

- `problems/` – statements, starter code, `tests.json`, editorials
- `Practice/` – test runner (now with `--json` / `--limit=N` for the UI)
- `tools/testaudit/` – Python tooling that audits and improves the test suites (development only)
- `Server/` – ASP.NET minimal-API server (no NuGet packages needed): serves the UI, compiles and runs solutions
- `web/` – the UI (plain HTML/CSS/JS)

## Third-party

- [Monaco Editor](https://github.com/microsoft/monaco-editor) (MIT) – the VS Code editor, vendored in `web/vendor/monaco`
- [marked](https://github.com/markedjs/marked) (MIT) – Markdown rendering, vendored in `web/vendor/marked`
- Problem statements/starter code: [neenza/leetcode-problems](https://github.com/neenza/leetcode-problems); tests: [newfacade/LeetCodeDataset](https://github.com/newfacade/LeetCodeDataset). Problem text belongs to LeetCode; personal study use only.
