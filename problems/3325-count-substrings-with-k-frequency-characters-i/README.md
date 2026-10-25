# 3325. Count Substrings With K-Frequency Characters I
**Difficulty:** Medium  
**Topics:** Hash Table, String, Sliding Window
**Link (online only):** https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times.

**Example 1:**
```
Input: s = "abacb", k = 2
Output: 4
Explanation:
The valid substrings are:
```

**Example 2:**
```
Input: s = "abcde", k = 1
Output: 15
Explanation:
All substrings are valid because every character appears at least once.
```

**Constraints:**
- 1 <= s.length <= 3000
- 1 <= k <= s.length
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Fix the <code>left</code> index of the substring.
2. For the fixed <code>left</code> index, find the first <code>right</code> index for which substring <code>s[left..right]</code> satisfies the condition.
3. Every substring that starts at <code>left</code> and ends after <code>right</code> satisfies the condition.

</details>
