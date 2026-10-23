# 3593. Minimum Increments to Equalize Leaf Paths
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Tree, Depth-First Search
**Link (online only):** https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

You are given an integer n and an undirected tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an edge from node ui to vi .
Each node i has an associated cost given by cost[i], representing the cost to traverse that node.
The score of a path is defined as the sum of the costs of all nodes along the path.
Your goal is to make the scores of all root-to-leaf paths equal by increasing the cost of any number of nodes by any non-negative amount.
Return the minimum number of nodes whose cost must be increased to make all root-to-leaf path scores equal.

**Example 1:**
```
Input: n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]
Output: 1
Explanation:

There are two root-to-leaf paths:
To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2. Only one node is increased, so the output is 1.
```

**Example 2:**
```
Input: n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]
Output: 0
Explanation:

There is only one root-to-leaf path:
Path 0 → 1 → 2 has a score of 5 + 1 + 4 = 10 .
Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.
```

**Example 3:**
```
Input: n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]
Output: 1
Explanation:

There are three root-to-leaf paths:
To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.
```

**Constraints:**
- 2 <= n <= 105
- edges.length == n - 1
- edges[i] == [ui, vi]
- 0 <= ui, vi < n
- cost.length == n
- 1 <= cost[i] <= 109
- The input is generated such that edges represents a valid tree.

<details><summary>Hints</summary>

1. Every root-to-leaf path's score must be raised to <code>maxLeafCost</code>, the maximum sum among all root-to-leaf paths.
2. For each <code>node</code>, compute <code>minIncrease[node]</code>, the minimum additional cost required so that every root-to-leaf path passing through that <code>node</code> reaches <code>maxLeafCost</code>.
3. The final answer, <code>ans</code>, is the count of <code>nodes</code> for which <code>minIncrease[node]</code> differs from <code>minIncrease[parent]</code>.

</details>
