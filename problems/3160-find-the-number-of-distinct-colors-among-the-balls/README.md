# 3160. Find the Number of Distinct Colors Among the Balls
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Simulation
**Link (online only):** https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

You are given an integer limit and a 2D array queries of size n x 2.
There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of colors among the balls.
Return an array result of length n, where result[i] denotes the number of colors after ith query.
Note that when answering a query, lack of a color will not be considered as a color.

**Example 1:**
```
Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
Output: [1,2,2,3]
Explanation:
```

**Example 2:**
```
Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
Output: [1,2,2,3,4]
Explanation:
```

**Constraints:**
- 1 <= limit <= 109
- 1 <= n == queries.length <= 105
- queries[i].length == 2
- 0 <= queries[i][0] <= limit
- 1 <= queries[i][1] <= 109

<details><summary>Hints</summary>

1. Use two HashMaps to maintain the color of each ball and the set of balls with each color.

</details>
