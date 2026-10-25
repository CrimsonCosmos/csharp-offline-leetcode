# 3524. Find X Value of Array I
**Difficulty:** Medium  
**Topics:** Array, Math, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/find-x-value-of-array-i/

You are given an array of positive integers nums, and a positive integer k.
You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.
You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.
Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.

**Example 1:**
```
Input: nums = [1,2,3,4,5], k = 3
Output: [9,2,4]
Explanation:
```

**Example 2:**
```
Input: nums = [1,2,4,8,16,32], k = 4
Output: [18,1,2,0]
Explanation:
```

**Example 3:**
```
Input: nums = [1,1,2,1,1], k = 2
Output: [9,6]
```

**Constraints:**
- 1 <= nums[i] <= 109
- 1 <= nums.length <= 105
- 1 <= k <= 5

<details><summary>Hints</summary>

1. Use dynamic programming.
2. Define <code>dp[i][r]</code> as the count of subarrays ending at index <code>i</code> whose product modulo <code>k</code> equals <code>r</code>.
3. Compute <code>dp[i][r]</code> for each index <code>i</code> in <code>nums</code> and sum over all indices to get the final counts for each remainder.

</details>
