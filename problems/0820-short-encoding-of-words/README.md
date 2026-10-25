# 820. Short Encoding of Words
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Trie
**Link (online only):** https://leetcode.com/problems/short-encoding-of-words/

A valid encoding of an array of words is any reference string s and array of indices indices such that:
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

**Example 1:**
```
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
```

**Example 2:**
```
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
```

**Constraints:**
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- words[i] consists of only lowercase letters.

