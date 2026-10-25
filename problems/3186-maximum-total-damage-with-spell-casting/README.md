# 3186. Maximum Total Damage With Spell Casting
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Two Pointers, Binary Search, Dynamic Programming, Sorting, Counting
**Link (online only):** https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

A magician has various spells.
You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
Each spell can be cast only once.
Return the maximum possible total damage that a magician can cast.

**Example 1:**
```
Input: power = [1,1,3,4]
Output: 6
Explanation:
The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
```

**Example 2:**
```
Input: power = [7,1,6,6]
Output: 13
Explanation:
The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
```

**Constraints:**
- 1 <= power.length <= 105
- 1 <= power[i] <= 109

<details><summary>Hints</summary>

1. If we ever decide to use some spell with power <code>x</code>, then we will use all spells with power <code>x</code>.
2. Think of dynamic programming.
3. <code>dp[i][j]</code> represents the maximum damage considering up to the <code>i</code>-th unique spell and <code>j</code> represents the number of spells skipped (up to 3 as per constraints).

</details>
