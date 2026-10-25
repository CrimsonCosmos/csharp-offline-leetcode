# 809. Expressive Words
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, String
**Link (online only):** https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling. For example:
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".
You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.
Return the number of query strings that are stretchy.

**Example 1:**
```
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
```

**Example 2:**
```
Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
```

**Constraints:**
- 1 <= s.length, words.length <= 100
- 1 <= words[i].length <= 100
- s and words[i] consist of lowercase letters.

