# 3567. Minimum Absolute Difference in Sliding Submatrix
**Difficulty:** Medium  
**Topics:** Array, Sorting, Matrix
**Link (online only):** https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

You are given an m x n integer matrix grid and an integer k.
For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.
Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.
Note: If all elements in the submatrix have the same value, the answer will be 0.

**Example 1:**
```
Input: grid = [[1,8],[3,-2]], k = 2
Output: [[2]]
Explanation:
```

**Example 2:**
```
Input: grid = [[3,-1]], k = 1
Output: [[0,0]]
Explanation:
```

**Example 3:**
```
Input: grid = [[1,-2,3],[2,3,5]], k = 2
Output: [[1,2]]
Explanation:
```

**Constraints:**
- 1 <= m == grid.length <= 30
- 1 <= n == grid[i].length <= 30
- -105 <= grid[i][j] <= 105
- 1 <= k <= min(m, n)

<details><summary>Hints</summary>

1. Use bruteforce over the submatrices

</details>
