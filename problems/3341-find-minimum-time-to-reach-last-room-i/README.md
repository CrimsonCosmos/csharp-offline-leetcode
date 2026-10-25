# 3341. Find Minimum Time to Reach Last Room I
**Difficulty:** Medium  
**Topics:** Array, Graph, Heap (Priority Queue), Matrix, Shortest Path
**Link (online only):** https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

There is a dungeon with n x m rooms arranged as a grid.
You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds after which the room opens and can be moved to. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.

**Example 1:**
```
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
```

**Example 2:**
```
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
```

**Example 3:**
```
Input: moveTime = [[0,1],[1,2]]
Output: 3
```

**Constraints:**
- 2 <= n == moveTime.length <= 50
- 2 <= m == moveTime[i].length <= 50
- 0 <= moveTime[i][j] <= 109

<details><summary>Hints</summary>

1. Use shortest path algorithms.

</details>
