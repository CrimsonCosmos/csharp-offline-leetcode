# 2857. Count Pairs of Points With Distance k
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Bit Manipulation
**Link (online only):** https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

You are given a 2D integer array coordinates and an integer k, where coordinates[i] = [xi, yi] are the coordinates of the ith point in a 2D plane.
We define the distance between two points (x1, y1) and (x2, y2) as (x1 XOR x2) + (y1 XOR y2) where XOR is the bitwise XOR operation.
Return the number of pairs (i, j) such that i < j and the distance between points i and j is equal to k.

**Example 1:**
```
Input: coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5
Output: 2
Explanation: We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.
```

**Example 2:**
```
Input: coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0
Output: 10
Explanation: Any two chosen pairs will have a distance of 0. There are 10 ways to choose two pairs.
```

**Constraints:**
- 2 <= coordinates.length <= 50000
- 0 <= xi, yi <= 106
- 0 <= k <= 100

<details><summary>Hints</summary>

1. <div class="_1l1MA">Suppose that <code>x = x<sub>1</sub> XOR x<sub>2</sub></code> and y = y<sub>1</sub> XOR y<sub>2</sub> then we can get <code>x<sub>2</sub> = x XOR x<sub>1</sub></code> and <code>y<sub>2</sub> = y XOR y<sub>1</sub></code>.</div>
2. <div class="_1l1MA">We are supposed to have k = x + y so we can get <code>x<sub>2</sub> = x XOR x<sub>1</sub></code> and <code>y<sub>2</sub> = (k - x) XOR y<sub>1</sub></code>.</div>
3. <div class="_1l1MA">We can iterate over all possible values of <code>x</code> and count the number of points <code>(x<sub>1</sub>, x<sub>2</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code>.</div>

</details>
