# 2550. Count Collisions of Monkeys on a Polygon
**Difficulty:** Medium  
**Topics:** Math, Recursion
**Link (online only):** https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

There is a regular convex polygon with n vertices. The vertices are labeled from 0 to n - 1 in a clockwise direction, and each vertex has exactly one monkey. The following figure shows a convex polygon of 6 vertices.
Simultaneously, each monkey moves to a neighboring vertex. A collision happens if at least two monkeys reside on the same vertex after the movement or intersect on an edge.
Return the number of ways the monkeys can move so that at least one collision happens. Since the answer may be very large, return it modulo 109 + 7.

**Example 1:**
```
Input: n = 3
Output: 6
Explanation:
There are 8 total possible movements. Two ways such that they collide at some point are:
```

**Example 2:**
```
Input: n = 4
Output: 14
```

**Constraints:**
- 3 <= n <= 109

<details><summary>Hints</summary>

1. Try counting the number of ways in which the monkeys will not collide.

</details>
