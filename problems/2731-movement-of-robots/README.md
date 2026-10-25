# 2731. Movement of Robots
**Difficulty:** Medium  
**Topics:** Array, Brainteaser, Sorting, Prefix Sum
**Link (online only):** https://leetcode.com/problems/movement-of-robots/

Some robots are standing on an infinite number line with their initial coordinates given by a 0-indexed integer array nums and will start moving once given the command to move. The robots will move a unit distance each second.
You are given a string s denoting the direction in which robots will move on command. 'L' means the robot will move towards the left side or negative side of the number line, whereas 'R' means the robot will move towards the right side or positive side of the number line.
If two robots collide, they will start moving in opposite directions.
Return the sum of distances between all the pairs of robots d seconds after the command. Since the sum can be very large, return it modulo 109 + 7.
Note:

**Example 1:**
```
Input: nums = [-2,0,2], s = "RLL", d = 3
Output: 8
Explanation: 
After 1 second, the positions are [-1,-1,1]. Now, the robot at index 0 will move left, and the robot at index 1 will move right.
After 2 seconds, the positions are [-2,0,0]. Now, the robot at index 1 will move left, and the robot at index 2 will move right.
After 3 seconds, the positions are [-3,-1,1].
The distance between the robot at index 0 and 1 is abs(-3 - (-1)) = 2.
The distance between the robot at index 0 and 2 is abs(-3 - 1) = 4.
The distance between the robot at index 1 and 2 is abs(-1 - 1) = 2.
The sum of the pairs of all distances = 2 + 4 + 2 = 8.
```

**Example 2:**
```
Input: nums = [1,0], s = "RL", d = 2
Output: 5
Explanation: 
After 1 second, the positions are [2,-1].
After 2 seconds, the positions are [3,-2].
The distance between the two robots is abs(-2 - 3) = 5.
```

**Constraints:**
- 2 <= nums.length <= 105
- -2 * 109 <= nums[i] <= 2 * 109
- 0 <= d <= 109
- nums.length == s.length
- s consists of 'L' and 'R' only
- nums[i] will be unique.

<details><summary>Hints</summary>

1. Observe that if you ignore collisions, the resultant positions of robots after d seconds would be the same.
2. After d seconds, sort the ending positions and use prefix sum to calculate the distance sum.

</details>
