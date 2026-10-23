# 3462. Maximum Sum With at Most K Elements
**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting, Heap (Priority Queue), Matrix
**Link (online only):** https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k. The task is to find the maximum sum of at most k elements from the matrix grid such that:
Return the maximum sum.

**Example 1:**
```
Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2
Output: 7
Explanation:
```

**Example 2:**
```
Input: grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3
Output: 21
Explanation:
```

**Constraints:**
- n == grid.length == limits.length
- m == grid[i].length
- 1 <= n, m <= 500
- 0 <= grid[i][j] <= 105
- 0 <= limits[i] <= m
- 0 <= k <= min(n * m, sum(limits))

<details><summary>Hints</summary>

1. Sort each row in descending order and extract the top <code>limits[i]</code> elements.
2. Use a max-heap to efficiently pick the largest <code>k</code> elements across all rows.

</details>
