# 3418. Maximum Amount of Money Robot Can Earn
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Matrix
**Link (online only):** https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.
The grid contains a value coins[i][j] in each cell:
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.
Note: The robot's total coins can be negative.
Return the maximum profit the robot can gain on the route.

**Example 1:**
```
Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
Output: 8
Explanation:
An optimal path for maximum coins is:
```

**Example 2:**
```
Input: coins = [[10,10,10],[10,10,10]]
Output: 40
Explanation:
An optimal path for maximum coins is:
```

**Constraints:**
- m == coins.length
- n == coins[i].length
- 1 <= m, n <= 500
- -1000 <= coins[i][j] <= 1000

<details><summary>Hints</summary>

1. Use Dynamic Programming.
2. Let <code>dp[i][j][k]</code> denote the maximum amount of money a robot can earn by starting at cell <code>(i,j)</code> and having neutralized <code>k</code> robbers.

</details>
