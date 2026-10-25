# 3228. Maximum Number of Operations to Move Ones to the End
**Difficulty:** Medium  
**Topics:** String, Greedy, Counting
**Link (online only):** https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

You are given a binary string s.
You can perform the following operation on the string any number of times:
Return the maximum number of operations that you can perform.

**Example 1:**
```
Input: s = "1001101"
Output: 4
Explanation:
We can perform the following operations:
```

**Example 2:**
```
Input: s = "00111"
Output: 0
```

**Constraints:**
- 1 <= s.length <= 105
- s[i] is either '0' or '1'.

<details><summary>Hints</summary>

1. It is optimal to perform the operation on the lowest index possible each time.
2. Traverse the string from left to right and perform the operation every time it is possible.

</details>
