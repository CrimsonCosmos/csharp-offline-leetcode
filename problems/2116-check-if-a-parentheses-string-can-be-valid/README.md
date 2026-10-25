# 2116. Check if a Parentheses String Can Be Valid
**Difficulty:** Medium  
**Topics:** String, Stack, Greedy
**Link (online only):** https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
Return true if you can make s a valid parentheses string. Otherwise, return false.

**Example 1:**
```
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
```

**Example 2:**
```
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
```

**Example 3:**
```
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
```

**Example 4:**
```
Input: s = "(((())(((())", locked = "111111010111"
Output: true
Explanation: locked permits us to change s[6] and s[8]. 
We change s[6] and s[8] to ')' to make s valid.
```

**Constraints:**
- n == s.length == locked.length
- 1 <= n <= 105
- s[i] is either '(' or ')'.
- locked[i] is either '0' or '1'.

<details><summary>Hints</summary>

1. Can an odd length string ever be valid?
2. From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?
3. After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?

</details>
