# 3163. String Compression III
**Difficulty:** Medium  
**Topics:** String
**Link (online only):** https://leetcode.com/problems/string-compression-iii/

Given a string word, compress it using the following algorithm:
Return the string comp.

**Example 1:**
```
Input: word = "abcde"
Output: "1a1b1c1d1e"
Explanation:
Initially, comp = "" . Apply the operation 5 times, choosing "a" , "b" , "c" , "d" , and "e" as the prefix in each operation.
For each prefix, append "1" followed by the character to comp .
```

**Example 2:**
```
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"
Explanation:
Initially, comp = "" . Apply the operation 3 times, choosing "aaaaaaaaa" , "aaaaa" , and "bb" as the prefix in each operation.
```

**Constraints:**
- 1 <= word.length <= 2 * 105
- word consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Each time, just cut the same character in prefix up to at max 9 times. It’s always better to cut a bigger prefix.

</details>
