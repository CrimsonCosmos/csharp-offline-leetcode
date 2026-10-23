# 3376. Minimum Time to Break Locks I
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Backtracking, Bit Manipulation, Depth-First Search, Bitmask
**Link (online only):** https://leetcode.com/problems/minimum-time-to-break-locks-i/

Bob is stuck in a dungeon and must break n locks, each requiring some amount of energy to break. The required energy for each lock is stored in an array called strength where strength[i] indicates the energy needed to break the ith lock.
To break a lock, Bob uses a sword with the following characteristics:
Your task is to determine the minimum time in minutes required for Bob to break all n locks and escape the dungeon.
Return the minimum time required for Bob to break all n locks.

**Example 1:**
```
Input: strength = [3,4,1], k = 1
Output: 4
Explanation:
The locks cannot be broken in less than 4 minutes; thus, the answer is 4.
```

**Example 2:**
```
Input: strength = [2,5,4], k = 2
Output: 5
Explanation:
The locks cannot be broken in less than 5 minutes; thus, the answer is 5.
```

**Constraints:**
- n == strength.length
- 1 <= n <= 8
- 1 <= K <= 10
- 1 <= strength[i] <= 106

<details><summary>Hints</summary>

1. Try all <code>n!</code> permutation ways of breaking the locks.

</details>
