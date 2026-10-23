# 3546. Equal Sum Grid Partition I
**Difficulty:** Medium  
**Topics:** Array, Matrix, Enumeration, Prefix Sum
**Link (online only):** https://leetcode.com/problems/equal-sum-grid-partition-i/

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
Return true if such a partition exists; otherwise return false.

**Example 1:**
```
Input: grid = [[1,4],[2,3]]
Output: true
Explanation:

A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true .
```

**Example 2:**
```
Input: grid = [[1,3],[2,4]]
Output: false
Explanation:
No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false .
```

**Constraints:**
- 1 <= m == grid.length <= 105
- 1 <= n == grid[i].length <= 105
- 2 <= m * n <= 105
- 1 <= grid[i][j] <= 105

<details><summary>Hints</summary>

1. There are two types of cuts: a <code>horizontal</code> cut or a <code>vertical</code> cut.
2. For a <code>horizontal</code> cut at row <code>r</code> (0 <= r <m - 1), split <code>grid</code> into rows 0...r vs. r+1...m-1 and compare their sums.
3. For a <code>vertical</code> cut at column <code>c</code> (0 <= c < n - 1), split <code>grid</code> into columns 0...c vs. c+1...n-1 and compare their sums.
4. Brute‑force all possible <code>r</code> and <code>c</code> cuts; if any yields equal section sums, return <code>true</code>.

</details>
