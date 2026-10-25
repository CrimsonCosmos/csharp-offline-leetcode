# 1253. Reconstruct a 2-Row Binary Matrix
**Difficulty:** Medium  
**Topics:** Array, Greedy, Matrix
**Link (online only):** https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

Given the following details of a matrix with n columns and 2 rows :
Your task is to reconstruct the matrix with upper, lower and colsum.
Return it as a 2-D integer array.
If there are more than one valid solution, any of them will be accepted.
If no valid solution exists, return an empty 2-D array.

**Example 1:**
```
Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
```

**Example 2:**
```
Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
```

**Example 3:**
```
Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
```

**Constraints:**
- 1 <= colsum.length <= 10^5
- 0 <= upper, lower <= colsum.length
- 0 <= colsum[i] <= 2

<details><summary>Hints</summary>

1. You cannot do anything about colsum[i] = 2 case or colsum[i] = 0 case. Then you put colsum[i] = 1 case to the upper row until upper has reached. Then put the rest into lower row.
2. Fill 0 and 2 first, then fill 1 in the upper row or lower row in turn but be careful about exhausting permitted 1s in each row.

</details>
