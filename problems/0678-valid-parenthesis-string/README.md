# 678. Valid Parenthesis String
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Stack, Greedy
**Link (online only):** https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "(*)"
Output: true
```

**Example 3:**
```
Input: s = "(*))"
Output: true
```

**Constraints:**
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.

<details><summary>Hints</summary>

1. Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
2. DP[i][j] represents whether the substring s[i:j] is valid.
3. Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
4. How about using 2 stacks instead of 1? Think about it.

</details>
