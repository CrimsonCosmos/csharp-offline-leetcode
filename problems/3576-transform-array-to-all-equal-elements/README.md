# 3576. Transform Array to All Equal Elements
**Difficulty:** Medium  
**Topics:** Array, Greedy
**Link (online only):** https://leetcode.com/problems/transform-array-to-all-equal-elements/

You are given an integer array nums of size n containing only 1 and -1, and an integer k.
You can perform the following operation at most k times:
Note that you can choose the same index i more than once in different operations.
Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.

**Example 1:**
```
Input: nums = [1,-1,1,-1,1], k = 3
Output: true
Explanation:
We can make all elements in the array equal in 2 operations as follows:
```

**Example 2:**
```
Input: nums = [-1,-1,-1,1,1,1], k = 5
Output: false
Explanation:
It is not possible to make all array elements equal in at most 5 operations.
```

**Constraints:**
- 1 <= n == nums.length <= 105
- nums[i] is either -1 or 1.
- 1 <= k <= n

<details><summary>Hints</summary>

1. Try converting all elements to 1 and separately to -1. For each case, calculate the minimum number of operations needed.
2. Use a greedy approach: scan the array from left to right and apply an operation only when needed to fix mismatches.

</details>
