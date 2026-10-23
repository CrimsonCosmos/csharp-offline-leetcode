# 966. Vowel Spellchecker
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String
**Link (online only):** https://leetcode.com/problems/vowel-spellchecker/

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
For a given query word, the spell checker handles two categories of spelling mistakes:
In addition, the spell checker operates under the following precedence rules:
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

**Example 1:**
```
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

**Example 2:**
```
Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
```

**Constraints:**
- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- wordlist[i] and queries[i] consist only of only English letters.

