# 2522. Partition String Into Substrings With Values at Most K
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

You are given a string s consisting of digits from 1 to 9 and an integer k.
A partition of a string s is called good if:
Return the minimum number of substrings in a good partition of s. If no good partition of s exists, return -1.
Note that:

**Example 1:**
```
Input: s = "165462", k = 60
Output: 4
Explanation: We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.
```

**Example 2:**
```
Input: s = "238182", k = 5
Output: -1
Explanation: There is no good partition for this string.
```

**Constraints:**
- 1 <= s.length <= 105
- s[i] is a digit from '1' to '9'.
- 1 <= k <= 109

