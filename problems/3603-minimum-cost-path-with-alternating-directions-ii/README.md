# 3603. Minimum Cost Path with Alternating Directions II
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Matrix
**Link (online only):** https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

You are given two integers m and n representing the number of rows and columns of a grid, respectively.
The cost to enter cell (i, j) is defined as (i + 1) * (j + 1).
You are also given a 2D integer array waitCost where waitCost[i][j] defines the cost to wait on that cell.
The path will always begin by entering cell (0, 0) on move 1 and paying the entrance cost.
At each step, you follow an alternating pattern:
Return the minimum total cost required to reach (m - 1, n - 1).

**Example 1:**
```
Input: m = 1, n = 2, waitCost = [[1,2]]
Output: 3
Explanation:
The optimal path is:
Thus, the total cost is 1 + 2 = 3 .
```

**Example 2:**
```
Input: m = 2, n = 2, waitCost = [[3,5],[2,4]]
Output: 9
Explanation:
The optimal path is:
Thus, the total cost is 1 + 2 + 2 + 4 = 9 .
```

**Example 3:**
```
Input: m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]
Output: 16
Explanation:
The optimal path is:
Thus, the total cost is 1 + 2 + 1 + 4 + 2 + 6 = 16 .
```

**Constraints:**
- 1 <= m, n <= 105
- 2 <= m * n <= 105
- waitCost.length == m
- waitCost[0].length == n
- 0 <= waitCost[i][j] <= 105

<details><summary>Hints</summary>

1. Use dynamic programming
2. Observe that you need to wait at each cell except the first and last
3. Transition: <code>dp[i][j]</code> <- min(<code>dp[i‑1][j]</code>, <code>dp[i][j‑1]</code>) + <code>waitCost[i][j]</code> + (<code>i+1</code>)*(<code>j+1</code>)
4. The answer is <code>dp[m‑1][n‑1]</code> - <code>waitCost[m‑1][n‑1]</code>

</details>
