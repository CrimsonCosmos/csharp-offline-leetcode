# 3388. Count Beautiful Splits in an Array
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/count-beautiful-splits-in-an-array/

You are given an array nums.
A split of an array nums is beautiful if:
Return the number of ways you can make this split.

**Example 1:**
```
Input: nums = [1,1,2,1]
Output: 2
Explanation:
The beautiful splits are:
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: 0
Explanation:
There are 0 beautiful splits.
```

**Constraints:**
- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 50

<details><summary>Hints</summary>

1. Use 2D dynamic programming to find the maximum matching prefix.

</details>
