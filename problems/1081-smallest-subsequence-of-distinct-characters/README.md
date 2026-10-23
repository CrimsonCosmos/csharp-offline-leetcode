# 1081. Smallest Subsequence of Distinct Characters
**Difficulty:** Medium  
**Topics:** String, Stack, Greedy, Monotonic Stack
**Link (online only):** https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

**Example 1:**
```
Input: s = "bcabc"
Output: "abc"
```

**Example 2:**
```
Input: s = "cbacdcbc"
Output: "acdb"
```

**Constraints:**
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

<details><summary>Hints</summary>

1. Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

</details>
