# 3025. Find the Number of Ways to Place People I
**Difficulty:** Medium  
**Topics:** Array, Math, Geometry, Sorting, Enumeration
**Link (online only):** https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
Count the number of pairs of points (A, B), where
Return the count.

**Example 1:**
```
Input: points = [[1,1],[2,2],[3,3]]
Output: 0
Explanation:

There is no way to choose A and B so A is on the upper left side of B .
```

**Example 2:**
```
Input: points = [[6,2],[4,4],[2,6]]
Output: 2
Explanation:
```

**Example 3:**
```
Input: points = [[3,1],[1,3],[1,1]]
Output: 2
Explanation:
```

**Constraints:**
- 2 <= n <= 50
- points[i].length == 2
- 0 <= points[i][0], points[i][1] <= 50
- All points[i] are distinct.

<details><summary>Hints</summary>

1. We can enumerate all the upper-left and lower-right corners.
2. If the upper-left corner is <code>(x1, y1)</code> and lower-right corner is <code>(x2, y2)</code>, check that there is no point <code>(x, y)</code> such that <code>x1 <= x <= x2</code> and <code>y2 <= y <= y1</code>.

</details>
