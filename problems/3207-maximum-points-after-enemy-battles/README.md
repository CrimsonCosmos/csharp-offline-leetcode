# 3207. Maximum Points After Enemy Battles
**Difficulty:** Medium  
**Topics:** Array, Greedy
**Link (online only):** https://leetcode.com/problems/maximum-points-after-enemy-battles/

You are given an integer array enemyEnergies denoting the energy values of various enemies.
You are also given an integer currentEnergy denoting the amount of energy you have initially.
You start with 0 points, and all the enemies are unmarked initially.
You can perform either of the following operations zero or multiple times to gain points:
Return an integer denoting the maximum points you can get in the end by optimally performing operations.

**Example 1:**
```
Input: enemyEnergies = [3,2,2], currentEnergy = 2
Output: 3
Explanation:
The following operations can be performed to get 3 points, which is the maximum:
```

**Example 2:**
```
Input: enemyEnergies = [2] , currentEnergy = 10
Output: 5
Explanation:
Performing the first operation 5 times on enemy 0 results in the maximum number of points.
```

**Constraints:**
- 1 <= enemyEnergies.length <= 105
- 1 <= enemyEnergies[i] <= 109
- 0 <= currentEnergy <= 109

<details><summary>Hints</summary>

1. The problem can be solved greedily.
2. Mark all the others except the smallest one first.
3. Use the smallest one to increase the energy.
4. Note that the initial energy should be no less than the smallest enemy.

</details>
