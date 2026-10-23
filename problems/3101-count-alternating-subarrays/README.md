# 3101. Count Alternating Subarrays
**Difficulty:** Medium  
**Topics:** Array, Math
**Link (online only):** https://leetcode.com/problems/count-alternating-subarrays/

You are given a binary array nums.
We call a subarray alternating if no two adjacent elements in the subarray have the same value.
Return the number of alternating subarrays in nums.

**Example 1:**
```
Input: nums = [0,1,1,1]
Output: 5
Explanation:
The following subarrays are alternating: [0] , [1] , [1] , [1] , and [0,1] .
```

**Example 2:**
```
Input: nums = [1,0,1,0]
Output: 10
Explanation:
Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.
```

**Constraints:**
- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

<details><summary>Hints</summary>

1. Try using dynamic programming.
2. Let <code>dp[i]</code> be the number of alternating subarrays ending at index <code>i</code>.
3. The final answer is the sum of <code>dp[i]</code> over all  indices <code>i</code> from <code>0</code> to <code>n - 1</code>.

</details>
