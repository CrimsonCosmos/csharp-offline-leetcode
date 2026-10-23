# 3179. Find the N-th Value After K Seconds
**Difficulty:** Medium  
**Topics:** Array, Math, Simulation, Combinatorics, Prefix Sum
**Link (online only):** https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

You are given two integers n and k.
Initially, you start with an array a of n integers where a[i] = 1 for all 0 <= i <= n - 1. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, a[0] remains the same, a[1] becomes a[0] + a[1], a[2] becomes a[0] + a[1] + a[2], and so on.
Return the value of a[n - 1] after k seconds.
Since the answer may be very large, return it modulo 109 + 7.

**Example 1:**
```
Input: n = 4, k = 5
Output: 56
Explanation:
```

**Example 2:**
```
Input: n = 5, k = 3
Output: 35
Explanation:
```

**Constraints:**
- 1 <= n, k <= 1000

<details><summary>Hints</summary>

1. Calculate the prefix sum array of <code>nums</code>, <code>k</code> times.

</details>
