# 874. Walking Robot Simulation
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Simulation
**Link (online only):** https://leetcode.com/problems/walking-robot-simulation/

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.
Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).
Note:

**Example 1:**
```
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation:
The robot starts at (0, 0) :
The furthest point the robot ever gets from the origin is (3, 4) , which squared is 3 2 + 4 2 = 25 units away.
```

**Example 2:**
```
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation:
The robot starts at (0, 0) :
The furthest point the robot ever gets from the origin is (1, 8) , which squared is 1 2 + 8 2 = 65 units away.
```

**Example 3:**
```
Input: commands = [6,-1,-1,6], obstacles = [[0,0]]
Output: 36
Explanation:
The robot starts at (0, 0) :
The furthest point the robot ever gets from the origin is (0, 6) , which squared is 6 2 = 36 units away.
```

**Constraints:**
- 1 <= commands.length <= 104
- commands[i] is either -2, -1, or an integer in the range [1, 9].
- 0 <= obstacles.length <= 104
- -3 * 104 <= xi, yi <= 3 * 104
- The answer is guaranteed to be less than 231.

