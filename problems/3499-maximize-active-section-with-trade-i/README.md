# 3499. Maximize Active Section with Trade I
**Difficulty:** Medium  
**Topics:** String, Enumeration
**Link (online only):** https://leetcode.com/problems/maximize-active-section-with-trade-i/

You are given a binary string s of length n, where:
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
Return the maximum number of active sections in s after making the optimal trade.
Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

**Example 1:**
```
Input: s = "01"
Output: 1
Explanation:
Because there is no block of '1' s surrounded by '0' s, no valid trade is possible. The maximum number of active sections is 1.
```

**Example 2:**
```
Input: s = "0100"
Output: 4
Explanation:
```

**Example 3:**
```
Input: s = "1000100"
Output: 7
Explanation:
```

**Example 4:**
```
Input: s = "01010"
Output: 4
Explanation:
```

**Constraints:**
- 1 <= n == s.length <= 105
- s[i] is either '0' or '1'

<details><summary>Hints</summary>

1. Split the string into several zero-one segments.
2. For each one-segment, if it has two neighbors (i.e., it is surrounded by two zero-segments), the total sum of their lengths is one of the candidates for <code>delta</code>.
3. Find the maximum <code>delta</code> and add it to the total number of ones in the string.

</details>
