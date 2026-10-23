# 3403. Find the Lexicographically Largest String From the Box I
**Difficulty:** Medium  
**Topics:** Two Pointers, String, Enumeration
**Link (online only):** https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

You are given a string word, and an integer numFriends.
Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
Find the lexicographically largest string from the box after all the rounds are finished.

**Example 1:**
```
Input: word = "dbca", numFriends = 2
Output: "dbc"
Explanation:
All possible splits are:
```

**Example 2:**
```
Input: word = "gggg", numFriends = 4
Output: "g"
Explanation:
The only possible split is: "g" , "g" , "g" , and "g" .
```

**Constraints:**
- 1 <= word.length <= 5 * 103
- word consists only of lowercase English letters.
- 1 <= numFriends <= word.length

<details><summary>Hints</summary>

1. Find lexicographically largest substring of size <code>n - numFriends + 1</code> or less starting at every index.

</details>
