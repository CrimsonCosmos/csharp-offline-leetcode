# 3532. Path Existence Queries in a Graph I
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Binary Search, Union Find, Graph
**Link (online only):** https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.
You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.
An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).
You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.
Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.

**Example 1:**
```
Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
Output: [true,false]
Explanation:
```

**Example 2:**
```
Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
Output: [false,false,true,true]
Explanation:
The resulting graph is:
```

**Constraints:**
- 1 <= n == nums.length <= 105
- 0 <= nums[i] <= 105
- nums is sorted in non-decreasing order.
- 0 <= maxDiff <= 105
- 1 <= queries.length <= 105
- queries[i] == [ui, vi]
- 0 <= ui, vi < n

<details><summary>Hints</summary>

1. How do the connected components look? Do they appear in segments (i.e., are they continuous)?
2. Preprocess the connected components.

</details>
