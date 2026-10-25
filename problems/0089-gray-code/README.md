# 89. Gray Code
**Difficulty:** Medium  
**Topics:** Math, Backtracking, Bit Manipulation
**Link (online only):** https://leetcode.com/problems/gray-code/

An n-bit gray code sequence is a sequence of 2n integers where:
Given an integer n, return any valid n-bit gray code sequence.

**Example 1:**
```
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
```

**Example 2:**
```
Input: n = 1
Output: [0,1]
```

**Constraints:**
- 1 <= n <= 16

