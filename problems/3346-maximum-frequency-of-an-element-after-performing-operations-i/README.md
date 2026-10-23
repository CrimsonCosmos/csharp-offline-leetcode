# 3346. Maximum Frequency of an Element After Performing Operations I
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Sliding Window, Sorting, Prefix Sum
**Link (online only):** https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

You are given an integer array nums and two integers k and numOperations.
You must perform an operation numOperations times on nums, where in each operation you:
Return the maximum possible frequency of any element in nums after performing the operations.

**Example 1:**
```
Input: nums = [1,4,5], k = 1, numOperations = 2
Output: 2
Explanation:
We can achieve a maximum frequency of two by:
```

**Example 2:**
```
Input: nums = [5,11,20,20], k = 5, numOperations = 1
Output: 2
Explanation:
We can achieve a maximum frequency of two by:
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105
- 0 <= k <= 105
- 0 <= numOperations <= nums.length

<details><summary>Hints</summary>

1. Sort the array and try each value in range as a candidate.

</details>
