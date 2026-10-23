# 1286. Iterator for Combination
**Difficulty:** Medium  
**Topics:** String, Backtracking, Design, Iterator
**Link (online only):** https://leetcode.com/problems/iterator-for-combination/

Design the CombinationIterator class:

**Example 1:**
```
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
```

**Constraints:**
- 1 <= combinationLength <= characters.length <= 15
- All the characters of characters are unique.
- At most 104 calls will be made to next and hasNext.
- It is guaranteed that all calls of the function next are valid.

<details><summary>Hints</summary>

1. Generate all combinations as a preprocessing.
2. Use bit masking to generate all the combinations.

</details>
