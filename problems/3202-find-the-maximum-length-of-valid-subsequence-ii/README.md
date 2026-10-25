# 3202. Find the Maximum Length of Valid Subsequence II
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

A subsequence sub of nums with length x is called valid if it satisfies:

**Example 1:**
```
Input: nums = [1,2,3,4,5], k = 2
Output: 5
Explanation:
The longest valid subsequence is [1, 2, 3, 4, 5] .
```

**Example 2:**
```
Input: nums = [1,4,2,3,1,4], k = 3
Output: 4
Explanation:
The longest valid subsequence is [1, 4, 1, 4] .
```

**Constraints:**
- 2 <= nums.length <= 103
- 1 <= nums[i] <= 107
- 1 <= k <= 103

<details><summary>Hints</summary>

1. Fix the value of <code>(subs[0] + subs[1]) % k</code> from the <code>k</code> possible values. Let it be <code>val</code>.
2. Let <code>dp[i]</code> store the maximum length of a subsequence with its last element <code>x</code> such that <code>x % k == i</code>.
3. Answer for a subsequence ending at index <code>y</code> is <code>dp[(k + val - (y % k)) % k] + 1</code>.

</details>
