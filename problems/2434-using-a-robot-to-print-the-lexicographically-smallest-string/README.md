# 2434. Using a Robot to Print the Lexicographically Smallest String
**Difficulty:** Medium  
**Topics:** Hash Table, String, Stack, Greedy
**Link (online only):** https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
Return the lexicographically smallest string that can be written on the paper.

**Example 1:**
```
Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
```

**Example 2:**
```
Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
```

**Example 3:**
```
Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
```

**Constraints:**
- 1 <= s.length <= 105
- s consists of only English lowercase letters.

<details><summary>Hints</summary>

1. If there are some character “a” ’ s in the string, they can be written on paper before anything else.
2. Every character in the string before the last “a” should be written in reversed order.
3. After the robot writes every “a” on paper, the same holds for other characters “b”, ”c”, …etc.

</details>
