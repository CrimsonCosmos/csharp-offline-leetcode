# 1849. Splitting a String Into Descending Consecutive Values
**Difficulty:** Medium  
**Topics:** String, Backtracking, Enumeration
**Link (online only):** https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

You are given a string s that consists of only digits.
Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.
Return true if it is possible to split s​​​​​​ as described above, or false otherwise.
A substring is a contiguous sequence of characters in a string.

**Example 1:**
```
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.
```

**Example 2:**
```
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
```

**Example 3:**
```
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.
```

**Constraints:**
- 1 <= s.length <= 20
- s only consists of digits.

<details><summary>Hints</summary>

1. One solution is to try all possible splits using backtrack
2. Look out for trailing zeros in string

</details>
