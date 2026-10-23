# 3350. Adjacent Increasing Subarrays Detection II
**Difficulty:** Medium  
**Topics:** Array, Binary Search
**Link (online only):** https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
Return the maximum possible value of k.
A subarray is a contiguous non-empty sequence of elements within an array.

**Example 1:**
```
Input: nums = [2,5,7,8,9,2,3,4,3,1]
Output: 3
Explanation:
```

**Example 2:**
```
Input: nums = [1,2,3,4,4,4,4,5,6,7]
Output: 2
Explanation:
```

**Constraints:**
- 2 <= nums.length <= 2 * 105
- -109 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Find the boundaries between strictly increasing subarrays.
2. Can we use binary search?

</details>
