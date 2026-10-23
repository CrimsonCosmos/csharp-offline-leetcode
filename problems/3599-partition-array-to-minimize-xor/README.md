# 3599. Partition Array to Minimize XOR
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Bit Manipulation, Prefix Sum
**Link (online only):** https://leetcode.com/problems/partition-array-to-minimize-xor/

You are given an integer array nums and an integer k.
Your task is to partition nums into k non-empty subarrays. For each subarray, compute the bitwise XOR of all its elements.
Return the minimum possible value of the maximum XOR among these k subarrays.

**Example 1:**
```
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The optimal partition is [1] and [2, 3] .
The maximum XOR among the subarrays is 1, which is the minimum possible.
```

**Example 2:**
```
Input: nums = [2,3,3,2], k = 3
Output: 2
Explanation:
The optimal partition is [2] , [3, 3] , and [2] .
The maximum XOR among the subarrays is 2, which is the minimum possible.
```

**Example 3:**
```
Input: nums = [1,1,2,3,1], k = 2
Output: 0
Explanation:
The optimal partition is [1, 1] and [2, 3, 1] .
The maximum XOR among the subarrays is 0, which is the minimum possible.
```

**Constraints:**
- 1 <= nums.length <= 250
- 1 <= nums[i] <= 109
- 1 <= k <= n

<details><summary>Hints</summary>

1. Use dynamic programming.
2. Precompute <code>pre[i] = nums[0] ^ … ^ nums[i-1]</code> so any subarray XOR is <code>pre[r] ^ pre[l]</code>.
3. Define <code>dp[i][j]</code> = minimum possible “max‑XOR” when splitting the first <code>i</code> elements into <code>j</code> parts.
4. For each <code>dp[i][j]</code>, try all splits <code>t < i</code> and take the minimum over <code>max(dp[t][j-1], pre[i] ^ pre[t])</code>.

</details>
