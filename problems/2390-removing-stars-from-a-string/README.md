# 2390. Removing Stars From a String
**Difficulty:** Medium  
**Topics:** String, Stack, Simulation
**Link (online only):** https://leetcode.com/problems/removing-stars-from-a-string/

You are given a string s, which contains stars *.
In one operation, you can:
Return the string after all stars have been removed.
Note:

**Example 1:**
```
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```

**Example 2:**
```
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
```

**Constraints:**
- 1 <= s.length <= 105
- s consists of lowercase English letters and stars *.
- The operation above can be performed on s.

<details><summary>Hints</summary>

1. What data structure could we use to efficiently perform these removals?
2. Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack.

</details>
