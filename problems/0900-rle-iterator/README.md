# 900. RLE Iterator
**Difficulty:** Medium  
**Topics:** Array, Design, Counting, Iterator
**Link (online only):** https://leetcode.com/problems/rle-iterator/

We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.
Given a run-length encoded array, design an iterator that iterates through it.
Implement the RLEIterator class:

**Example 1:**
```
Input
["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output
[null, 8, 8, 5, -1]

Explanation
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].
rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
but the second term did not exist. Since the last term exhausted does not exist, we return -1.
```

**Constraints:**
- 2 <= encoding.length <= 1000
- encoding.length is even.
- 0 <= encoding[i] <= 109
- 1 <= n <= 109
- At most 1000 calls will be made to next.

