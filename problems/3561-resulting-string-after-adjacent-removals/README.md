# 3561. Resulting String After Adjacent Removals
**Difficulty:** Medium  
**Topics:** String, Stack, Simulation
**Link (online only):** https://leetcode.com/problems/resulting-string-after-adjacent-removals/

You are given a string s consisting of lowercase English letters.
You must repeatedly perform the following operation while the string s has at least two consecutive characters:
Return the resulting string after no more operations can be performed.
Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.

**Example 1:**
```
Input: s = "abc"
Output: "c"
Explanation:
```

**Example 2:**
```
Input: s = "adcb"
Output: ""
Explanation:
```

**Example 3:**
```
Input: s = "zadb"
Output: "db"
Explanation:
```

**Constraints:**
- 1 <= s.length <= 105
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Traverse the string from left to right and use a stack to perform the removals.

</details>
