# 2840. Check if Strings Can be Made Equal With Operations II
**Difficulty:** Medium  
**Topics:** Hash Table, String, Sorting
**Link (online only):** https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
You can apply the following operation on any of the two strings any number of times:
Return true if you can make the strings s1 and s2 equal, and false otherwise.

**Example 1:**
```
Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
```

**Example 2:**
```
Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.
```

**Constraints:**
- n == s1.length == s2.length
- 1 <= n <= 105
- s1 and s2 consist only of lowercase English letters.

<details><summary>Hints</summary>

1. <div class="_1l1MA">Characters in two positions can be swapped if and only if the two positions have the same parity.</div>
2. <div class="_1l1MA">To be able to make the two strings equal, the characters at even and odd positions in the strings should be the same.</div>

</details>
