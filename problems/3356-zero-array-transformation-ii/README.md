# 3356. Zero Array Transformation II
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Prefix Sum
**Link (online only):** https://leetcode.com/problems/zero-array-transformation-ii/

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
Each queries[i] represents the following action on nums:
A Zero Array is an array with all its elements equal to 0.
Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

**Example 1:**
```
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
```

**Example 2:**
```
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 0 <= nums[i] <= 5 * 105
- 1 <= queries.length <= 105
- queries[i].length == 3
- 0 <= li <= ri < nums.length
- 1 <= vali <= 5

<details><summary>Hints</summary>

1. Can we apply binary search here?
2. Utilize a difference array to optimize the processing of queries.

</details>
