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
- Code autosaves to `userdata/code/` (back it up with the ☁ button, see below); progress and submission history live in `userdata/progress.json` (git-ignored). Delete `userdata/` to start fresh.
- Tick **ignore result order** for problems that accept answers in any order.
- Problems without a test suite can be marked solved by hand. Problems tagged *examples only* use the statement's examples as tests; design problems (e.g. LRU Cache) run the example operation sequences.
- Known gaps: 10 problems that need a `Node` class (n-ary trees, quad trees, random-pointer lists, ...) and a few random/interactive problems have no tests (their `Node`/`Employee` classes are now uncommented so the code compiles, but you check them against the statement examples).

The tests started as LLM-generated cases from the open LeetCodeDataset, not LeetCode's hidden tests. They have since been audited (invalid cases removed, large and generated cases added, in-place and design problems verified); see [TEST_QUALITY.md](TEST_QUALITY.md) for what was done and what it does and does not prove, and [PRACTICE_PACK_README.md](PRACTICE_PACK_README.md) for the original caveats. The original CLI (`./run.sh 2`, `.\run.ps1 2`) still works.

## Cloud backup (free, optional)

Click the **☁** icon (top right) once to back up `userdata/` (your code, progress and submission history) to a private Git repository. After that it backs up automatically in the background every time a problem is **Accepted**, and the icon turns green. A failed backup never interrupts you; it just shows red with the reason.

1. Install [git](https://git-scm.com) if you don't have it (macOS asks for the developer tools the first time).
2. Create an **empty private** repository on GitHub (free), e.g. `leetcode-backup`.
3. Make sure git can push there from this computer (GitHub Desktop, `gh auth login`, or a saved credential; if unsure, run `git ls-remote <repo url>` in a terminal once and sign in).
4. Click ☁ and paste the repository URL (HTTPS or SSH).

**New computer:** set up the same repo URL in the same way; your backed-up code and progress are merged in (if both sides have different data, the local copy wins, nothing is deleted). **Turn off:** click ☁, type `off`. Each solve is one git commit, so the full history is in the repo.

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
