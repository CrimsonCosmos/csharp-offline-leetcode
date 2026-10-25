# 3514. Number of Unique XOR Triplets II
**Difficulty:** Medium  
**Topics:** Array, Math, Bit Manipulation, Enumeration
**Link (online only):** https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

You are given an integer array nums.
A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
Return the number of unique XOR triplet values from all possible triplets (i, j, k).

**Example 1:**
```
Input: nums = [1,3]
Output: 2
Explanation:
The possible XOR triplet values are:
The unique XOR values are {1, 3} . Thus, the output is 2.
```

**Example 2:**
```
Input: nums = [6,7,8,9]
Output: 4
Explanation:
The possible XOR triplet values are {6, 7, 8, 9} . Thus, the output is 4.
```

**Constraints:**
- 1 <= nums.length <= 1500
- 1 <= nums[i] <= 1500

<details><summary>Hints</summary>

1. What is the maximum possible XOR value achievable by any triplet?
2. Let the maximum possible XOR value be stored in <code>max_xor</code>.
3. For each index <code>i</code>, consider all pairs of indices <code>(j, k)</code> such that <code>i <= j <= k</code>. For each such pair, compute the triplet XOR as <code>nums[i] XOR nums[j] XOR nums[k]</code>.
4. You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index <code>i</code>, compute XORs of pairs <code>(j, k)</code> in <code>O(n<sup>2</sup>)</code> time instead of checking all three indices independently.
5. Finally, count the number of unique XOR values obtained from all triplets.

</details>
