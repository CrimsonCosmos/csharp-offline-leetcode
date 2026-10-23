# Test-suite audit tooling

The test cases shipped with the pack are LLM-generated inputs whose expected values were produced by running reference
solutions (LeetCodeDataset). They are not LeetCode's hidden tests, so this folder contains tooling that measures how
trustworthy and how thorough they are, deterministically and offline (after the one-time `fetch_reference.py`).

Everything here is development tooling (Python 3.10+, `pip install sortedcontainers`). The app itself does not need it.

| Script | What it does |
|---|---|
| `fetch_reference.py` | Builds `reference.json.gz`: Python reference solutions (`completion`) and an independent second solution (`response`) for every problem, from the same dataset the tests came from. Already committed. |
| `constraints.py` | Parses the README *Constraints* section (numeric bounds on values / lengths / node counts, alphabets, uniqueness, sortedness, length relations, `n == nums.length` aliases...) and checks every test input against it. Superscripts were flattened in the READMEs (`10^4` became `104`), so the most permissive reading is used: a test is flagged only if it violates the constraint under every reading. |
| `clean_tests.py` | Removes tests that cannot occur on LeetCode (constraint violations) and exact duplicates. Removed cases are logged in `report/removed_tests.json.gz`. |
| `audit.py` | Cross-validates expected values (reference and second solution vs. `tests.json`) and **mutation-tests** each suite: seeded mutants of the reference solution (flipped comparisons, off-by-one constants, swapped operators, negated conditions, `min`/`max` swaps, `len(x)-1`...) are run against the tests; a mutant that passes every test *survived*. `--family B` uses a second, disjoint set of operators (flipped inequality direction, deleted statements, flipped booleans) that is never used to guide generation. |
| `generate.py` | For problems with a single canonical answer, searches for new inputs (perturbing existing ones) that kill surviving mutants, plus a few large "performance" inputs. A candidate is accepted only if it satisfies the README constraints and shape invariants mined from the existing tests, fits the C# parameter and return types, and the reference and the second solution agree on it deterministically. Tests are tagged `"g"` in `tests.json`. |
| `fix_inplace.py` | The 11 in-place problems had tests that only checked "does not throw". Stores the reference's final state of the mutated argument as `e` and `"inplaceArg"`; the C# runner now verifies it. |
| `fix_lca.py`, `fix_small.py` | Problem-specific repairs (LCA node references; exhaustive small domains; structured generators for 1093 and 1583). |
| `check_csharp.py` | Compiles each problem's stub and runs the C# runner in `--check` mode to prove every test deserializes into the real C# types (nothing silently skipped). |
| `finalize.py` | Updates per-problem audit counters, `unordered` hints and the *Tests* column of `INDEX.md`. |
| `survivors.py` | Prints the surviving mutants of one problem as diffs (to judge equivalent mutants vs. missing tests). |

Reproduce: `python3 audit.py --jobs 4` (about 10 minutes), results in `report/`.
