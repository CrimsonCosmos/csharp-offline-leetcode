# 3608. Minimum Time for K Connected Components
**Difficulty:** Medium  
**Topics:** Binary Search, Union Find, Graph, Sorting
**Link (online only):** https://leetcode.com/problems/minimum-time-for-k-connected-components/

You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges, where edges[i] = [ui, vi, timei] indicates an undirected edge between nodes ui and vi that can be removed at timei.
You are also given an integer k.
Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t, the graph contains at least k connected components.
Return the minimum time t.
A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

**Example 1:**
```
Input: n = 2, edges = [[0,1,3]], k = 2
Output: 3
Explanation:
```

**Example 2:**
```
Input: n = 3, edges = [[0,1,2],[1,2,4]], k = 3
Output: 4
Explanation:
```

**Example 3:**
```
Input: n = 3, edges = [[0,2,5]], k = 2
Output: 0
Explanation:
```

**Constraints:**
- 1 <= n <= 105
- 0 <= edges.length <= 105
- edges[i] = [ui, vi, timei]
- 0 <= ui, vi < n
- ui != vi
- 1 <= timei <= 109
- 1 <= k <= n
- There are no duplicate edges.

<details><summary>Hints</summary>

1. Binary-search the smallest <code>t</code> such that, after removing all edges with <code>time <= t</code>, the graph splits into >= <code>k</code> connected components.

</details>
