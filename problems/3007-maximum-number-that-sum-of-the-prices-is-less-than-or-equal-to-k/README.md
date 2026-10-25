# 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K
**Difficulty:** Medium  
**Topics:** Binary Search, Dynamic Programming, Bit Manipulation
**Link (online only):** https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

You are given an integer k and an integer x. The price of a number num is calculated by the count of set bits at positions x, 2x, 3x, etc., in its binary representation, starting from the least significant bit. The following table contains examples of how price is calculated.
The accumulated price of num is the total price of numbers from 1 to num. num is considered cheap if its accumulated price is less than or equal to k.
Return the greatest cheap number.

**Example 1:**
```
Input: k = 9, x = 1
Output: 6
Explanation:
As shown in the table below, 6 is the greatest cheap number.
```

**Example 2:**
```
Input: k = 7, x = 2
Output: 9
Explanation:
As shown in the table below, 9 is the greatest cheap number.
```

**Constraints:**
- 1 <= k <= 1015
- 1 <= x <= 8

<details><summary>Hints</summary>

1. Binary search the answer.
2. In each step of the binary search you should calculate the number of the set bits in the <code>i<sup>th</sup></code> position. Then calculate the sum of them.

</details>
