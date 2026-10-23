# 1003. Check If Word Is Valid After Substitutions
**Difficulty:** Medium  
**Topics:** String, Stack
**Link (online only):** https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

Given a string s, determine if it is valid.
A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
Return true if s is a valid string, otherwise, return false.

**Example 1:**
```
Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
```

**Example 2:**
```
Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
```

**Example 3:**
```
Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
```

**Constraints:**
- 1 <= s.length <= 2 * 104
- s consists of letters 'a', 'b', and 'c'

