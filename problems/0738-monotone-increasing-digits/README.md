# 738. Monotone Increasing Digits
**Difficulty:** Medium  
**Topics:** Math, Greedy
**Link (online only):** https://leetcode.com/problems/monotone-increasing-digits/

An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

**Example 1:**
```
Input: n = 10
Output: 9
```

**Example 2:**
```
Input: n = 1234
Output: 1234
```

**Example 3:**
```
Input: n = 332
Output: 299
```

**Constraints:**
- 0 <= n <= 109

<details><summary>Hints</summary>

1. Build the answer digit by digit, adding the largest possible one that would make the number still less than or equal to N.

</details>
