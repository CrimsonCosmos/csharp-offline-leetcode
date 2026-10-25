# 3366. Minimum Array Sum
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/minimum-array-sum/

You are given an integer array nums and three integers k, op1, and op2.
You can perform the following operations on nums:
Note: Both operations can be applied to the same index, but at most once each.
Return the minimum possible sum of all elements in nums after performing any number of operations.

**Example 1:**
```
Input: nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1
Output: 23
Explanation:
```

**Example 2:**
```
Input: nums = [2,4,3], k = 3, op1 = 2, op2 = 1
Output: 3
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 105
- 0 <= k <= 105
- 0 <= op1, op2 <= nums.length

<details><summary>Hints</summary>

1. Think of dynamic programming with states to track progress and remaining operations.
2. Use <code>dp[index][op1][op2]</code> where each state tracks progress at <code>index</code> with <code>op1</code> and <code>op2</code> operations left.
3. At each state, try applying only operation 1, only operation 2, both in sequence, or skip both to find optimal results.

</details>
