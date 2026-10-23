# 3531. Count Covered Buildings
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Sorting
**Link (online only):** https://leetcode.com/problems/count-covered-buildings/

You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
A building is covered if there is at least one building in all four directions: left, right, above, and below.
Return the number of covered buildings.

**Example 1:**
```
Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
Output: 1
Explanation:
```

**Example 2:**
```
Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
Output: 0
Explanation:
```

**Example 3:**
```
Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
Output: 1
Explanation:
```

**Constraints:**
- 2 <= n <= 105
- 1 <= buildings.length <= 105
- buildings[i] = [x, y]
- 1 <= x, y <= n
- All coordinates of buildings are unique.

<details><summary>Hints</summary>

1. Group buildings with the same x or y value together, and sort each group.
2. In each sorted list, the buildings that are not at the first or last positions are covered in that direction.

</details>
