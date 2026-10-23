# 3212. Count Submatrices With Equal Frequency of X and Y
**Difficulty:** Medium  
**Topics:** Array, Matrix, Prefix Sum
**Link (online only):** https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

**Example 1:**
```
Input: grid = [["X","Y","."],["Y",".","."]]
Output: 3
Explanation:
```

**Example 2:**
```
Input: grid = [["X","X"],["X","Y"]]
Output: 0
Explanation:
No submatrix has an equal frequency of 'X' and 'Y' .
```

**Example 3:**
```
Input: grid = [[".","."],[".","."]]
Output: 0
Explanation:
No submatrix has at least one 'X' .
```

**Constraints:**
- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 'X', 'Y', or '.'.

<details><summary>Hints</summary>

1. Replace <code>’X’</code> with 1, <code>’Y’</code> with -1 and <code>’.’</code> with 0.
2. You need to find how many submatrices <code>grid[0..x][0..y]</code> have a sum of 0 and at least one <code>’X’</code>.
3. Use prefix sum to calculate submatrices sum.

</details>
