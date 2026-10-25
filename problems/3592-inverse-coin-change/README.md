# 3592. Inverse Coin Change
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/inverse-coin-change/

You are given a 1-indexed integer array numWays, where numWays[i] represents the number of ways to select a total amount i using an infinite supply of some fixed coin denominations. Each denomination is a positive integer with value at most numWays.length.
However, the exact coin denominations have been lost. Your task is to recover the set of denominations that could have resulted in the given numWays array.
Return a sorted array containing unique integers which represents this set of denominations.
If no such set exists, return an empty array.

**Example 1:**
```
Input: numWays = [0,1,0,2,0,3,0,4,0,5]
Output: [2,4,6]
Explanation:
Input: numWays = [1,2,2,3,4]
Output: [1,2,5]
Explanation:
Example 3:
Input: numWays = [1,2,3,4,15]
Output: []
Explanation:
No set of denomination satisfies this array.
```

**Example 2:**
```
Input: numWays = [1,2,2,3,4]
Output: [1,2,5]
Explanation:
```

**Example 3:**
```
Input: numWays = [1,2,3,4,15]
Output: []
Explanation:
No set of denomination satisfies this array.
```

**Constraints:**
- 1 <= numWays.length <= 100
- 0 <= numWays[i] <= 2 * 108

<details><summary>Hints</summary>

1. Observe that for the smallest denomination <code>c</code>, you must have <code>numWays[c] == 1</code>.
2. Find the smallest <code>c > 0</code> with <code>numWays[c] == 1</code> and append <code>c</code> to your <code>ans</code> list.
3. "Remove" that coin’s contribution by doing, for each <code>s</code> from <code>c</code> up to <code>n</code>: numWays[s] -= numWays[s - c]
4. Repeat: pick the next smallest <code>c</code> with <code>numWays[c] == 1</code>, remove it, and so on.
5. At the end, if <code>numWays</code> is all zeros, your <code>ans</code> is valid; otherwise, return an empty array.

</details>
