# 478. Generate Random Point in a Circle
**Difficulty:** Medium  
**Topics:** Math, Geometry, Rejection Sampling, Randomized
**Link (online only):** https://leetcode.com/problems/generate-random-point-in-a-circle/

Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.
Implement the Solution class:

**Example 1:**
```
Input
["Solution", "randPoint", "randPoint", "randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
Output
[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

Explanation
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint(); // return [-0.02493, -0.38077]
solution.randPoint(); // return [0.82314, 0.38945]
solution.randPoint(); // return [0.36572, 0.17248]
```

**Constraints:**
- 0 < radius <= 108
- -107 <= x_center, y_center <= 107
- At most 3 * 104 calls will be made to randPoint.

