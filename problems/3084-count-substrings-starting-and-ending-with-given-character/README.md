# 3084. Count Substrings Starting and Ending with Given Character
**Difficulty:** Medium  
**Topics:** Math, String, Counting
**Link (online only):** https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

You are given a string s and a character c. Return the total number of substrings of s that start and end with c.

**Example 1:**
```
Input: s = "abada", c = "a"
Output: 6
Explanation: Substrings starting and ending with "a" are: " a bada" , " aba da" , " abada " , "ab a da" , "ab ada " , "abad a " .
```

**Example 2:**
```
Input: s = "zzz", c = "z"
Output: 6
Explanation: There are a total of 6 substrings in s and all start and end with "z" .
```

**Constraints:**
- 1 <= s.length <= 105
- s and c consist only of lowercase English letters.

<details><summary>Hints</summary>

1. Count the number of characters <code>'c'</code> in string <code>s</code>, let’s call it <code>m</code>.
2. We can select <code>2</code> numbers <code>i</code> and <code>j</code> such that <code>i <= j</code> are the start and end indices of substring. Note that <code>i</code> and <code>j</code> can be the same.
3. The answer is <code>m * (m + 1) / 2</code>.

</details>
