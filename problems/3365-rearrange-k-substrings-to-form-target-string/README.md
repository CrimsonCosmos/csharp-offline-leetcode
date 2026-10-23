# 3365. Rearrange K Substrings to Form Target String
**Difficulty:** Medium  
**Topics:** Hash Table, String, Sorting
**Link (online only):** https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

You are given two strings s and t, both of which are anagrams of each other, and an integer k.
Your task is to determine whether it is possible to split the string s into k equal-sized substrings, rearrange the substrings, and concatenate them in any order to create a new string that matches the given string t.
Return true if this is possible, otherwise, return false.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
A substring is a contiguous non-empty sequence of characters within a string.

**Example 1:**
```
Input: s = "abcd", t = "cdab", k = 2
Output: true
Explanation:
```

**Example 2:**
```
Input: s = "aabbcc", t = "bbaacc", k = 3
Output: true
Explanation:
```

**Example 3:**
```
Input: s = "aabbcc", t = "bbaacc", k = 2
Output: false
Explanation:
```

**Constraints:**
- 1 <= s.length == t.length <= 2 * 105
- 1 <= k <= s.length
- s.length is divisible by k.
- s and t consist only of lowercase English letters.
- The input is generated such that s and t are anagrams of each other.

<details><summary>Hints</summary>

1. Split <code>s</code> into <code>k</code> equal-sized substrings, use a map to track frequencies, and check if rearranging them can form <code>t</code>.

</details>
