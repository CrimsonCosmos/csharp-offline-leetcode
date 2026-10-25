# 3488. Closest Equal Element Queries
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Binary Search
**Link (online only):** https://leetcode.com/problems/closest-equal-element-queries/

You are given a circular array nums and an array queries.
For each query i, you have to find the following:
Return an array answer of the same size as queries, where answer[i] represents the result for query i.

**Example 1:**
```
Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
Output: [2,-1,3]
Explanation:
```

**Example 2:**
```
Input: nums = [1,2,3,4], queries = [0,1,2,3]
Output: [-1,-1,-1,-1]
Explanation:
Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.
```

**Constraints:**
- 1 <= queries.length <= nums.length <= 105
- 1 <= nums[i] <= 106
- 0 <= queries[i] < nums.length

<details><summary>Hints</summary>

1. Use a dictionary that maps each unique value in the array to a sorted list of its indices.
2. For each query, use binary search on the sorted indices list to find the nearest occurrences of the target value.

</details>
