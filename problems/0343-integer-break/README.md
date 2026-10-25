# 343. Integer Break
**Difficulty:** Medium  
**Topics:** Math, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/integer-break/

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**
```
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Constraints:**
- 2 <= n <= 58

<details><summary>Hints</summary>

1. There is a simple O(n) solution to this problem.
2. You may check the breaking results of <i>n</i> ranging from 7 to 10 to discover the regularities.

</details>
