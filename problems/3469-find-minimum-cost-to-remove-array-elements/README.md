# 3469. Find Minimum Cost to Remove Array Elements
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

You are given an integer array nums. Your task is to remove all elements from the array by performing one of the following operations at each step until nums is empty:
Return the minimum cost required to remove all the elements.

**Example 1:**
```
Input: nums = [6,2,8,4]
Output: 12
Explanation:
Initially, nums = [6, 2, 8, 4] .
The cost to remove all elements is 8 + 4 = 12 . This is the minimum cost to remove all elements in nums . Hence, the output is 12.
```

**Example 2:**
```
Input: nums = [2,1,3,3]
Output: 5
Explanation:
Initially, nums = [2, 1, 3, 3] .
The cost to remove all elements is 2 + 3 = 5 . This is the minimum cost to remove all elements in nums . Hence, the output is 5.
```

**Constraints:**
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 106

<details><summary>Hints</summary>

1. Can we use dynamic programming here?
2. Use dynamic programming. The process guarantees that the remaining elements form a prefix of the array with at most one previous element.
3. Define the state as <code>dp[i][j]</code>, where <code>i</code> represents the last remaining element and <code>j</code> represents the starting index of the current prefix.

</details>
