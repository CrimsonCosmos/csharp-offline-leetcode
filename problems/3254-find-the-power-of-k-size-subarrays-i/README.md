# 3254. Find the Power of K-Size Subarrays I
**Difficulty:** Medium  
**Topics:** Array, Sliding Window
**Link (online only):** https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

**Example 1:**
```
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
```

**Example 2:**
```
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]
```

**Example 3:**
```
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]
```

**Constraints:**
- 1 <= n == nums.length <= 500
- 1 <= nums[i] <= 105
- 1 <= k <= n

<details><summary>Hints</summary>

1. Can we use a brute force solution with nested loops and HashSet?

</details>
