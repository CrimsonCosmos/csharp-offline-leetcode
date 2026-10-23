# 3106. Lexicographically Smallest String After Operations With Constraint
**Difficulty:** Medium  
**Topics:** String, Greedy
**Link (online only):** https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

You are given a string s and an integer k.
Define a function distance(s1, s2) between two strings s1 and s2 of the same length n as:
For example, distance("ab", "cd") == 4, and distance("a", "z") == 1.
You can change any letter of s to any other lowercase English letter, any number of times.
Return a string denoting the lexicographically smallest string t you can get after some changes, such that distance(s, t) <= k.

**Example 1:**
```
Input: s = "zbbz", k = 3
Output: "aaaz"
Explanation:
Change s to "aaaz" . The distance between "zbbz" and "aaaz" is equal to k = 3 .
```

**Example 2:**
```
Input: s = "xaxcd", k = 4
Output: "aawcd"
Explanation:
The distance between "xaxcd" and "aawcd" is equal to k = 4.
```

**Example 3:**
```
Input: s = "lol", k = 0
Output: "lol"
Explanation:
It's impossible to change any character as k = 0 .
```

**Constraints:**
- 1 <= s.length <= 100
- 0 <= k <= 2000
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. The problem can be approached greedily.
2. For each index in order from <code>0</code> to <code>n - 1</code>, we try all letters from <code>'a'</code> to <code>'z'</code>, selecting the first one as long as the current total distance accumulated is not larger than <code>k</code>.

</details>
