# 3404. Count Special Subsequences
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Math, Enumeration
**Link (online only):** https://leetcode.com/problems/count-special-subsequences/

You are given an array nums consisting of positive integers.
A special subsequence is defined as a subsequence of length 4, represented by indices (p, q, r, s), where p < q < r < s. This subsequence must satisfy the following conditions:
Return the number of different special subsequences in nums.

**Example 1:**
```
Input: nums = [1,2,3,4,3,6,1]
Output: 1
Explanation:
There is one special subsequence in nums .
```

**Example 2:**
```
Input: nums = [3,4,3,4,3,4,3,4]
Output: 3
Explanation:
There are three special subsequences in nums .
```

**Constraints:**
- 7 <= nums.length <= 1000
- 1 <= nums[i] <= 1000

<details><summary>Hints</summary>

1. Count pairs where <code>nums[p] / nums[q]</code> equals <code>nums[s] / nums[r]</code>, using GCD to handle ratios efficiently.
2. Try iterating over <code>(p, q)</code> pairs and efficiently count valid <code>(r, s)</code> pairs with the same ratio.

</details>
