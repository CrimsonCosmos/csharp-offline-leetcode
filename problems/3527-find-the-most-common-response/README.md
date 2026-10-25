# 3527. Find the Most Common Response
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Counting
**Link (online only):** https://leetcode.com/problems/find-the-most-common-response/

You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.
Return the most common response across all days after removing duplicate responses within each responses[i]. If there is a tie, return the lexicographically smallest response.

**Example 1:**
```
Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
Output: "good"
Explanation:
```

**Example 2:**
```
Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
Output: "bad"
Explanation:
```

**Constraints:**
- 1 <= responses.length <= 1000
- 1 <= responses[i].length <= 1000
- 1 <= responses[i][j].length <= 10
- responses[i][j] consists of only lowercase English letters

<details><summary>Hints</summary>

1. Use a HashMap.

</details>
