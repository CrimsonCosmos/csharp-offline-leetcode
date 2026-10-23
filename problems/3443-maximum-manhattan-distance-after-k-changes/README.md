# 3443. Maximum Manhattan Distance After K Changes
**Difficulty:** Medium  
**Topics:** Hash Table, Math, String, Counting
**Link (online only):** https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.
Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

**Example 1:**
```
Input: s = "NWSE", k = 1
Output: 3
Explanation:
Change s[2] from 'S' to 'N' . The string s becomes "NWNE" .
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.
```

**Example 2:**
```
Input: s = "NSWWEW", k = 3
Output: 6
Explanation:
Change s[1] from 'S' to 'N' , and s[4] from 'E' to 'W' . The string s becomes "NNWWWW" .
The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.
```

**Constraints:**
- 1 <= s.length <= 105
- 0 <= k <= s.length
- s consists of only 'N', 'S', 'E', and 'W'.

<details><summary>Hints</summary>

1. We can brute force all the possible directions (NE, NW, SE, SW).
2. Change up to <code>k</code> characters to maximize the distance in the chosen direction.

</details>
