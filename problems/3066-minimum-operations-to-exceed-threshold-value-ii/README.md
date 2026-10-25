# 3066. Minimum Operations to Exceed Threshold Value II
**Difficulty:** Medium  
**Topics:** Array, Heap (Priority Queue), Simulation
**Link (online only):** https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

You are given a 0-indexed integer array nums, and an integer k.
You are allowed to perform some operations on nums, where in a single operation, you can:
Note that you can only apply the described operation if nums contains at least two elements.
Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

**Example 1:**
```
Input: nums = [2,11,10,1,3], k = 10
Output: 2
Explanation:
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.
```

**Example 2:**
```
Input: nums = [1,1,2,4,9], k = 20
Output: 4
Explanation:
At this stage, all the elements of nums are greater than 20 so we can stop.
It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20.
```

**Constraints:**
- 2 <= nums.length <= 2 * 105
- 1 <= nums[i] <= 109
- 1 <= k <= 109
- The input is generated such that an answer always exists. That is, after performing some number of operations, all elements of the array are greater than or equal to k.

<details><summary>Hints</summary>

1. Use priority queue to keep track of minimum elements.
2. Remove the minimum two elements, perform the operation, and insert the resulting number into the priority queue.

</details>
