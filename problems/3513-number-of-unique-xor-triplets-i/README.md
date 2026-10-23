# 3513. Number of Unique XOR Triplets I
**Difficulty:** Medium  
**Topics:** Array, Math, Bit Manipulation
**Link (online only):** https://leetcode.com/problems/number-of-unique-xor-triplets-i/

You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [1, n].
A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
Return the number of unique XOR triplet values from all possible triplets (i, j, k).

**Example 1:**
```
Input: nums = [1,2]
Output: 2
Explanation:
The possible XOR triplet values are:
The unique XOR values are {1, 2} , so the output is 2.
```

**Example 2:**
```
Input: nums = [3,1,2]
Output: 4
Explanation:
The possible XOR triplet values include:
The unique XOR values are {0, 1, 2, 3} , so the output is 4.
```

**Constraints:**
- 1 <= n == nums.length <= 105
- 1 <= nums[i] <= n
- nums is a permutation of integers from 1 to n.

<details><summary>Hints</summary>

1. What is the maximum and minimum value we can obtain using the given numbers?
2. Can we generate all numbers within that range?
3. For <code>n >= 3</code> we can obtain all numbers in <code>[0, 2^(msb(n) + 1) - 1]</code>, where <code>msb(n)</code> is the index of the most significant bit in <code>n</code>’s binary representation (i.e., the highest power of 2 less than or equal to <code>n</code>). Handle the case when <code>n <= 2</code> separately.

</details>
