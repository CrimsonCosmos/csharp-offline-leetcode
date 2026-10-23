# 3393. Count Paths With the Given XOR Value
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Bit Manipulation, Matrix
**Link (online only):** https://leetcode.com/problems/count-paths-with-the-given-xor-value/

You are given a 2D integer array grid with size m x n. You are also given an integer k.
Your task is to calculate the number of paths you can take from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1) satisfying the following constraints:
Return the total number of such paths.
Since the answer can be very large, return the result modulo 109 + 7.

**Example 1:**
```
Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11
Output: 3
Explanation:
The 3 paths are:
```

**Example 2:**
```
Input: grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2
Output: 5
Explanation:
The 5 paths are:
```

**Example 3:**
```
Input: grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10
Output: 0
```

**Constraints:**
- 1 <= m == grid.length <= 300
- 1 <= n == grid[r].length <= 300
- 0 <= grid[r][c] < 16
- 0 <= k < 16

<details><summary>Hints</summary>

1. Use DP.

</details>
