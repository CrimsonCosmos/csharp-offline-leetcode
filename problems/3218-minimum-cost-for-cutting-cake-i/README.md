# 3218. Minimum Cost for Cutting Cake I
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

There is an m x n cake that needs to be cut into 1 x 1 pieces.
You are given integers m, n, and two arrays:
In one operation, you can choose any piece of cake that is not yet a 1 x 1 square and perform one of the following cuts:
After the cut, the piece of cake is divided into two distinct pieces.
The cost of a cut depends only on the initial cost of the line and does not change.
Return the minimum total cost to cut the entire cake into 1 x 1 pieces.

**Example 1:**
```
Input: m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]
Output: 13
Explanation:

The total cost is 5 + 1 + 1 + 3 + 3 = 13 .
```

**Example 2:**
```
Input: m = 2, n = 2, horizontalCut = [7], verticalCut = [4]
Output: 15
Explanation:
The total cost is 7 + 4 + 4 = 15 .
```

**Constraints:**
- 1 <= m, n <= 20
- horizontalCut.length == m - 1
- verticalCut.length == n - 1
- 1 <= horizontalCut[i], verticalCut[i] <= 103

<details><summary>Hints</summary>

1. The intended solution uses Dynamic Programming.
2. Let <code>dp[sx][sy][tx][ty]</code> denote the minimum cost to cut the rectangle into <code>1 x 1</code> pieces.
3. Iterate on the row or column on which you will perform the next cut, after the cut, the current rectangle will be decomposed into two sub-rectangles.

</details>
