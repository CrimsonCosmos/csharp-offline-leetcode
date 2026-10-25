# 3176. Find the Maximum Length of a Good Subsequence I
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range [0, seq.length - 2] such that seq[i] != seq[i + 1].
Return the maximum possible length of a good subsequence of nums.

**Example 1:**
```
Input: nums = [1,2,1,1,3], k = 2
Output: 4
Explanation:
The maximum length subsequence is [ 1 , 2 , 1 , 1 ,3] .
```

**Example 2:**
```
Input: nums = [1,2,3,4,5,1], k = 0
Output: 2
Explanation:
The maximum length subsequence is [ 1 ,2,3,4,5, 1 ] .
```

**Constraints:**
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 109
- 0 <= k <= min(nums.length, 25)

<details><summary>Hints</summary>

1. The absolute values in <code>nums</code> don’t really matter. So we can remap the set of values to the range <code>[0, n - 1]</code>.
2. Let <code>dp[i][j]</code> be the length of the longest subsequence till index <code>j</code> with at most <code>i</code> positions such that <code>seq[i] != seq[i + 1]</code>.
3. For each value <code>x</code> from left to right, update <code>dp[i][x] = max(dp[i][x] + 1, dp[i - 1][y] + 1)</code>, where <code>y != x</code>.

</details>
