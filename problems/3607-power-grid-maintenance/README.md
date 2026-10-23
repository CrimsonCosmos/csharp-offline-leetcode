# 3607. Power Grid Maintenance
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Depth-First Search, Breadth-First Search, Union Find, Graph, Heap (Priority Queue), Ordered Set
**Link (online only):** https://leetcode.com/problems/power-grid-maintenance/

You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).
These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.
Initially, all stations are online (operational).
You are also given a 2D array queries, where each query is one of the following two types:
Return an array of integers representing the results of each query of type [1, x] in the order they appear.
Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

**Example 1:**
```
Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
Output: [3,2,3]
Explanation:
```

**Example 2:**
```
Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]
Output: [1,-1]
Explanation:
```

**Constraints:**
- 1 <= c <= 105
- 0 <= n == connections.length <= min(105, c * (c - 1) / 2)
- connections[i].length == 2
- 1 <= ui, vi <= c
- ui != vi
- 1 <= queries.length <= 2 * 105
- queries[i].length == 2
- queries[i][0] is either 1 or 2.
- 1 <= queries[i][1] <= c

<details><summary>Hints</summary>

1. Use DFS or BFS to assign each station a component ID
2. For each component, maintain a sorted set of online station IDs
3. For query <code>[2, x]</code>, remove <code>x</code> from the set of its component
4. For query <code>[1, x]</code>, if <code>x</code> is in its component’s set return <code>x</code>; otherwise if the set is non-empty return its smallest element; else return <code>-1</code>
5. Precompute all components and then handle each query in O(log n) time using the sorted sets

</details>
