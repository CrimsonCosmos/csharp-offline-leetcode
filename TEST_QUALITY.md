# How good are the test suites?

The pack's tests were LLM-generated inputs with expected values from reference solutions (not LeetCode's hidden tests).
They have been audited with the scripts in [`tools/testaudit`](tools/testaudit/README.md), which are deterministic and
reproducible. Summary of what was found and done:

## Problems found in the original suites (and fixed)

| Finding | Original | Now |
|---|---|---|
| Tests whose input **violates the README constraints** (lengths, value ranges, uniqueness, `n == nums.length`, node values...), which no LeetCode judge would ever send. A correct solution can fail them or time out on them. | 5,832 tests in 660 problems (4.8%), including arrays that are not really "rotated sorted", trees that are not BSTs, repeated edges | removed (logged in `tools/testaudit/report/removed_tests.json.gz`); every remaining test satisfies every constraint the checker understands |
| Duplicate inputs | 2,377 | removed |
| Tests the C# runner **silently skipped** (value does not fit `int`, etc.) | 272 in 47 problems | removed; `check_csharp.py` proves all 1,376 suites now deserialize into the real C# types with nothing skipped |
| **In-place problems** (Sort Colors, Rotate Image, ...) only checked "does not throw" | 11 problems | 10 are verified against the reference's final state (Wiggle Sort II has many valid outputs, so it still only checks that the code runs) |
| Lowest Common Ancestor (#236): expected values were all `null`, unusable | 20 broken tests | rebuilt: 71 tests, node references resolved by the runner |
| **No large inputs**: of the 521 problems whose constraints allow 10^4+ elements, none had a test with 1,000+ elements and 78% never exceeded 100 | 0 of 521 | 67% now have a large test (typically tens of thousands of elements; limited by repo size and the speed of the Python reference); tagged `"g":"perf"` and run with a 2 s limit so a quadratic solution fails |
| Problems with **no tests** (154) | 0 tests | 117 now have the examples from the statement as tests (`examples only` badge in the UI), including 46 "design" problems (class + operation sequence, new runner mode). The rest are random/interactive/unsupported-type problems. |
| Suites that were nearly empty after cleaning (e.g. #1093 had only invalid tests) | | topped up or regenerated with structured generators and exhaustive small domains |

## Evidence of thoroughness

* **Cross-validation.** Every remaining expected value equals the output of the dataset's reference solution, and of a second,
  independently written solution (disagreements: Wiggle Sort II, which accepts many answers, plus 2 inputs where the naive
  second solution times out).
* **Mutation testing.** 29,160 seeded mutants of the reference solutions (flipped comparisons, off-by-one constants,
  swapped operators, negated conditions, `len(x)-1`, `min`/`max`...) are run against each suite. **92.3%** are killed
  (held-out seed; 92.0% before the cleanup). A second, disjoint family of operators (flipped inequality direction,
  deleted statements, flipped booleans), which was never used to guide test generation, is killed **98.1%** of the time.
  The cleanup removed some accidental kills by invalid tests, so the scores are flat while the suites are now valid.
* **Surviving mutants are mostly equivalent.** Reading the diffs of the worst problems shows changes such as `[0]*(n+1)` ->
  `[0]*(n+2)` or `<` -> `<=` in a tie-breaking comparator. A search for inputs that distinguish a survivor from the original
  (3,000 perturbation attempts each) found killers for ~12% of them (187 new tests); the rest are likely equivalent.
* **Generated tests are only kept when** they satisfy the README constraints and the shape invariants mined from the existing
  tests, fit the C# types, and both reference solutions agree on them deterministically.

## What this does not prove

* These are not LeetCode's hidden tests; passing here does not guarantee acceptance on leetcode.com.
* 276 problems whose statement says "in any order" / "any valid answer" or contains guarantees the checker cannot verify
  ("the input is generated such that ...") were audited but got no generated tests (a generated input could be invalid).
  For "in any order" statements the UI defaults to order-insensitive comparison.
* Problems with several valid outputs that are not just reorderings can still mark a correct answer wrong.
* The constraint checker understands numeric bounds, lengths, alphabets, uniqueness, sortedness and length relations;
  other prose constraints are not checked.
* Eleven problems use `Node` classes the runner does not define (n-ary tree, quad tree, random pointer ...); they have no tests.
* Perf tests are limited by how fast the Python reference is, so n = 10^5 is often not reached.

Reproduce: see `tools/testaudit/README.md` (`python3 audit.py`, `python3 constraints.py`, `python3 bound_coverage.py`, `python3 check_csharp.py`).
