# 130. Surrounded Regions
**Difficulty:** Medium  
**Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
**Link (online only):** https://leetcode.com/problems/surrounded-regions/

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

**Example 1:**
```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
```

**Example 2:**
```
Input: board = [["X"]]
Output: [["X"]]
```

**Constraints:**
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

