# 3543. Maximum Weighted K-Edge Path
**Difficulty:** Medium  
**Topics:** Hash Table, Dynamic Programming, Graph
**Link (online only):** https://leetcode.com/problems/maximum-weighted-k-edge-path/

You are given an integer n and a Directed Acyclic Graph (DAG) with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, wi] indicates a directed edge from node ui to vi with weight wi.
You are also given two integers, k and t.
Your task is to determine the maximum possible sum of edge weights for any path in the graph such that:
Return the maximum possible sum of weights for such a path. If no such path exists, return -1.

**Example 1:**
```
Input: n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4
Output: 3
Explanation:
```

**Example 2:**
```
Input: n = 3, edges = [[0,1,2],[0,2,3]], k = 1, t = 3
Output: 2
Explanation:
```

**Example 3:**
```
Input: n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6
Output: -1
Explanation:
```

**Constraints:**
- 1 <= n <= 300
- 0 <= edges.length <= 300
- edges[i] = [ui, vi, wi]
- 0 <= ui, vi < n
- ui != vi
- 1 <= wi <= 10
- 0 <= k <= 300
- 1 <= t <= 600
- The input graph is guaranteed to be a DAG.
- There are no duplicate edges.

<details><summary>Hints</summary>

1. Use Dynamic Programming
2. How many paths and path sums are possible? Can we maintain the pathSums for a given path length ending at a particular node in a set?
3. The set <code>dp[i][j]</code> contains all possible path weights that end at node <code>i</code>, have total weight less than <code>T</code>, and consist of exactly <code>j</code> edges

</details>
