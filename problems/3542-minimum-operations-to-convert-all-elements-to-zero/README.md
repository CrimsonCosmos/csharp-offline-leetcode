# 3542. Minimum Operations to Convert All Elements to Zero
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Stack, Greedy, Monotonic Stack
**Link (online only):** https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.
In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.
Return the minimum number of operations required to make all elements in the array 0.

**Example 1:**
```
Input: nums = [0,2]
Output: 1
Explanation:
```

**Example 2:**
```
Input: nums = [3,1,2,1]
Output: 3
Explanation:
```

**Example 3:**
```
Input: nums = [1,2,1,2,1,2]
Output: 4
Explanation:
```

**Constraints:**
- 1 <= n == nums.length <= 105
- 0 <= nums[i] <= 105

<details><summary>Hints</summary>

1. Process the values in nums from smallest to largest (excluding 0).
2. For each target value v, identify its maximal contiguous segments (subarrays where nums[i] == v); each segment can be zeroed out in one operation.
3. After setting those segments to zero, dynamically update the remaining array and repeat with the next value.

</details>
