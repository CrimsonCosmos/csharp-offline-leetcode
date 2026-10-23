# 2711. Difference of Number of Distinct Values on Diagonals
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Matrix
**Link (online only):** https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

Given a 2D grid of size m x n, you should find the matrix answer of size m x n.
The cell answer[r][c] is calculated by looking at the diagonal values of the cell grid[r][c]:
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.
Return the matrix answer.

**Example 1:**
```
Input: grid = [[1,2,3],[3,1,5],[3,2,1]]
Output: Output: [[1,1,0],[1,0,1],[0,1,1]]
Explanation:
To calculate the answer cells:
```

**Example 2:**
```
Input: grid = [[1]]
Output: Output: [[0]]
```

**Constraints:**
- m == grid.length
- n == grid[i].length
- 1 <= m, n, grid[i][j] <= 50

<details><summary>Hints</summary>

1. Use the set to count the number of distinct elements on diagonals.

</details>
