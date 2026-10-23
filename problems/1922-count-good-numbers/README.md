# 1922. Count Good Numbers
**Difficulty:** Medium  
**Topics:** Math, Recursion
**Link (online only):** https://leetcode.com/problems/count-good-numbers/

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

**Example 1:**
```
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
```

**Example 2:**
```
Input: n = 4
Output: 400
```

**Example 3:**
```
Input: n = 50
Output: 564908303
```

**Constraints:**
- 1 <= n <= 1015

<details><summary>Hints</summary>

1. Is there a formula we can use to find the count of all the good numbers?
2. Exponentiation can be done very fast if we looked at the binary bits of n.

</details>
