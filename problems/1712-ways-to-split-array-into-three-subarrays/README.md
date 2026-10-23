# 1712. Ways to Split Array Into Three Subarrays
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Binary Search, Prefix Sum
**Link (online only):** https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

A split of an integer array is good if:
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

**Example 1:**
```
Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
```

**Example 2:**
```
Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
```

**Example 3:**
```
Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
```

**Constraints:**
- 3 <= nums.length <= 105
- 0 <= nums[i] <= 104

<details><summary>Hints</summary>

1. Create a prefix array to efficiently find the sum of subarrays.
2. As we are dividing the array into three subarrays, there are two "walls". Iterate over the right wall positions and find where the left wall could be for each right wall position.
3. Use binary search to find the left-most position and right-most position the left wall could be.

</details>
