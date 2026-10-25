# 3021. Alice and Bob Playing Flower Game
**Difficulty:** Medium  
**Topics:** Math
**Link (online only):** https://leetcode.com/problems/alice-and-bob-playing-flower-game/

Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, and y flowers in the anti-clockwise direction between them.
The game proceeds as follows:
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

**Example 1:**
```
Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
```

**Example 2:**
```
Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.
```

**Constraints:**
- 1 <= n, m <= 105

<details><summary>Hints</summary>

1. (x, y) is valid if and only if they have different parities.

</details>
