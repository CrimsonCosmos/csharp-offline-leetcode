# 3096. Minimum Levels to Gain More Points
**Difficulty:** Medium  
**Topics:** Array, Prefix Sum
**Link (online only):** https://leetcode.com/problems/minimum-levels-to-gain-more-points/

You are given a binary array possible of length n.
Alice and Bob are playing a game that consists of n levels. Some of the levels in the game are impossible to clear while others can always be cleared. In particular, if possible[i] == 0, then the ith level is impossible to clear for both the players. A player gains 1 point on clearing a level and loses 1 point if the player fails to clear it.
At the start of the game, Alice will play some levels in the given order starting from the 0th level, after which Bob will play for the rest of the levels.
Alice wants to know the minimum number of levels she should play to gain more points than Bob, if both players play optimally to maximize their points.
Return the minimum number of levels Alice should play to gain more points. If this is not possible, return -1.
Note that each player must play at least 1 level.

**Example 1:**
```
Input: possible = [1,0,1,0]
Output: 1
Explanation:
Let's look at all the levels that Alice can play up to:
Alice must play a minimum of 1 level to gain more points.
```

**Example 2:**
```
Input: possible = [1,1,1,1,1]
Output: 3
Explanation:
Let's look at all the levels that Alice can play up to:
Alice must play a minimum of 3 levels to gain more points.
```

**Example 3:**
```
Input: possible = [0,0]
Output: -1
Explanation:
The only possible way is for both players to play 1 level each. Alice plays level 0 and loses 1 point. Bob plays level 1 and loses 1 point. As both players have equal points, Alice can't gain more points than Bob.
```

**Constraints:**
- 2 <= n == possible.length <= 105
- possible[i] is either 0 or 1.

<details><summary>Hints</summary>

1. Change all <code>0</code> in possible array into <code>-1</code>.
2. We need to find the shortest non-empty prefix of the new possible array such that the sum of elements in it is strictly larger than the remaining part.

</details>
