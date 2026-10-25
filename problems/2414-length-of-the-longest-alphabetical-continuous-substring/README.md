# 2414. Length of the Longest Alphabetical Continuous Substring
**Difficulty:** Medium  
**Topics:** String
**Link (online only):** https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

**Example 1:**
```
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
```

**Example 2:**
```
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
```

**Constraints:**
- 1 <= s.length <= 105
- s consists of only English lowercase letters.

<details><summary>Hints</summary>

1. What is the longest possible continuous substring?
2. The size of the longest possible continuous substring is at most 26, so we can just brute force the answer.

</details>
