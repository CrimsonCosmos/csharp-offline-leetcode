# 3568. Minimum Moves to Clean the Classroom
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix
**Link (online only):** https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.
Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.
Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

**Example 1:**
```
Input: classroom = ["S.", "XL"], energy = 2
Output: 2
Explanation:
```

**Example 2:**
```
Input: classroom = ["LS", "RL"], energy = 4
Output: 3
Explanation:
```

**Example 3:**
```
Input: classroom = ["L.S", "RXL"], energy = 3
Output: -1
Explanation:
No valid path collects all 'L' .
```

**Constraints:**
- 1 <= m == classroom.length <= 20
- 1 <= n == classroom[i].length <= 20
- classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
- 1 <= energy <= 50
- There is exactly one 'S' in the grid.
- There are at most 10 'L' cells in the grid.

<details><summary>Hints</summary>

1. Use BFS with states <code>(x, y, mask, e, steps)</code>, initializing with <code>(sx, sy, 0, energy, 0)</code>, and for each move update <code>e</code> (–1 per step), update <code>mask</code> on 'L', reset <code>e=energy</code> on 'R', and return <code>steps</code> when <code>mask == fullMask</code>.
2. Maintain a 3D array <code>bestEnergy[x][y][mask]</code> storing the maximum <code>e</code> seen for each <code>(x,y,mask)</code> and skip any new state with <code>e <= bestEnergy[x][y][mask]</code> to prune.

</details>
