# 3473. Sum of K Subarrays With Length at Least M
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Prefix Sum
**Link (online only):** https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

You are given an integer array nums and two integers, k and m.
Return the maximum sum of k non-overlapping subarrays of nums, where each subarray has a length of at least m.

**Example 1:**
```
Input: nums = [1,2,-1,3,3,4], k = 2, m = 2
Output: 13
Explanation:
The optimal choice is:
The total sum is 10 + 3 = 13 .
```

**Example 2:**
```
Input: nums = [-10,3,-1,-2], k = 4, m = 1
Output: -10
Explanation:
The optimal choice is choosing each element as a subarray. The output is (-10) + 3 + (-1) + (-2) = -10 .
```

**Constraints:**
- 1 <= nums.length <= 2000
- -104 <= nums[i] <= 104
- 1 <= k <= floor(nums.length / m)
- 1 <= m <= 3

<details><summary>Hints</summary>

1. Dynamic Programming
2. Prefix Sum
3. Let <code>dp[i][j]</code> be the maximum sum with <code>i</code> subarrays for the first <code>j</code> elements

</details>
