# 3223. Minimum Length of String After Operations
**Difficulty:** Medium  
**Topics:** Hash Table, String, Counting
**Link (online only):** https://leetcode.com/problems/minimum-length-of-string-after-operations/

You are given a string s.
You can perform the following process on s any number of times:
Return the minimum length of the final string s that you can achieve.

**Example 1:**
```
Input: s = "abaacbcbb"
Output: 5
Explanation: We do the following operations:
```

**Example 2:**
```
Input: s = "aa"
Output: 2
Explanation: We cannot perform any operations, so we return the length of the original string.
```

**Constraints:**
- 1 <= s.length <= 2 * 105
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Only the frequency of each character matters in finding the final answer.
2. If a character occurs less than 3 times, we cannot perform any process with it.
3. Suppose there is a character that occurs at least 3 times in the string, we can repeatedly delete two of these characters until there are at most 2 occurrences left of it.

</details>
