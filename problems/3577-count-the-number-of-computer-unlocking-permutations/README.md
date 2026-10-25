# 3577. Count the Number of Computer Unlocking Permutations
**Difficulty:** Medium  
**Topics:** Array, Math, Brainteaser, Combinatorics
**Link (online only):** https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

You are given an array complexity of length n.
There are n locked computers in a room with labels from 0 to n - 1, each with its own unique password. The password of the computer i has a complexity complexity[i].
The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:
Find the number of permutations of [0, 1, 2, ..., (n - 1)] that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.
Since the answer may be large, return it modulo 109 + 7.
Note that the password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.

**Example 1:**
```
Input: complexity = [1,2,3]
Output: 2
Explanation:
The valid permutations are:
```

**Example 2:**
```
Input: complexity = [3,3,3,4,4,4]
Output: 0
Explanation:
There are no possible permutations which can unlock all computers.
```

**Constraints:**
- 2 <= complexity.length <= 105
- 1 <= complexity[i] <= 109

<details><summary>Hints</summary>

1. Ensure that the element at index 0 has the unique minimum complexity (no other element can match its value).
2. Fix index 0 as the first in the unlocking order.
3. The remaining indices from <code>1</code> to <code>n - 1</code> can then be arranged arbitrarily, yielding <code>factorial(n - 1)</code> possible orders.

</details>
