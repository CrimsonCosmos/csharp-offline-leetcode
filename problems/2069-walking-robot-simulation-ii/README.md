# 2069. Walking Robot Simulation II
**Difficulty:** Medium  
**Topics:** Design, Simulation
**Link (online only):** https://leetcode.com/problems/walking-robot-simulation-ii/

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".
The robot can be instructed to move for a specific number of steps. For each step, it does the following.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.
Implement the Robot class:

**Example 1:**
```
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"
```

**Constraints:**
- 2 <= width, height <= 100
- 1 <= num <= 105
- At most 104 calls in total will be made to step, getPos, and getDir.

<details><summary>Hints</summary>

1. The robot only moves along the perimeter of the grid. Can you think if modulus can help you quickly compute which cell it stops at?
2. After the robot moves one time, whenever the robot stops at some cell, it will always face a specific direction. i.e., The direction it faces is determined by the cell it stops at.
3. Can you precompute what direction it faces when it stops at each cell along the perimeter, and reuse the results?

</details>
