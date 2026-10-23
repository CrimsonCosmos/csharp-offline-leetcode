# 3122. Minimum Number of Operations to Satisfy Conditions
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Matrix
**Link (online only):** https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

You are given a 2D matrix grid of size m x n. In one operation, you can change the value of any cell to any non-negative number. You need to perform some operations such that each cell grid[i][j] is:
Return the minimum number of operations needed.

**Example 1:**
```
Input: grid = [[1,0,2],[1,0,2]]
Output: 0
Explanation:

All the cells in the matrix already satisfy the properties.
```

**Example 2:**
```
Input: grid = [[1,1,1],[0,0,0]]
Output: 3
Explanation:

The matrix becomes [[1,0,1],[1,0,1]] which satisfies the properties, by doing these 3 operations:
```

**Example 3:**
```
Input: grid = [[1],[2],[3]]
Output: 2
Explanation:

There is a single column. We can change the value to 1 in each cell using 2 operations.
```

**Constraints:**
- 1 <= n, m <= 1000
- 0 <= grid[i][j] <= 9

