# 2166. Design Bitset
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Design
**Link (online only):** https://leetcode.com/problems/design-bitset/

A Bitset is a data structure that compactly stores bits.
Implement the Bitset class:

**Example 1:**
```
Input
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
Output
[null, null, null, null, false, null, null, true, null, 2, "01010"]

Explanation
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1);     // the value at idx = 1 is updated to 1, so bitset = "01010". 
bs.flip();     // the value of each bit is flipped, so bitset = "10101". 
bs.all();      // return False, as not all values of the bitset are 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip();     // the value of each bit is flipped, so bitset = "11010". 
bs.one();      // return True, as there is at least 1 index with value 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count();    // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.
```

**Constraints:**
- 1 <= size <= 105
- 0 <= idx <= size - 1
- At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.
- At least one call will be made to all, one, count, or toString.
- At most 5 calls will be made to toString.

<details><summary>Hints</summary>

1. Note that flipping a bit twice does nothing.
2. In order to determine the value of a bit, consider how you can efficiently count the number of flips made on the bit since its latest update.

</details>
