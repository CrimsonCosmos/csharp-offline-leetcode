# 1765. Map of Highest Peak
**Difficulty:** Medium  
**Topics:** Array, Breadth-First Search, Matrix
**Link (online only):** https://leetcode.com/problems/map-of-highest-peak/

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
You must assign each cell a height in a way that follows these rules:
Find an assignment of heights such that the maximum height in the matrix is maximized.
Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/

**Example 1:**
```
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
```

**Example 2:**
```
Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
```

**Constraints:**
- m == isWater.length
- n == isWater[i].length
- 1 <= m, n <= 1000
- isWater[i][j] is 0 or 1.
- There is at least one water cell.

<details><summary>Hints</summary>

1. Set each water cell to be 0. The height of each cell is limited by its closest water cell.
2. Perform a multi-source BFS with all the water cells as sources.

</details>
