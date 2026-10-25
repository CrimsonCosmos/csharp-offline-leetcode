# 1781. Sum of Beauty of All Substrings
**Difficulty:** Medium  
**Topics:** Hash Table, String, Counting
**Link (online only):** https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
Given a string s, return the sum of beauty of all of its substrings.

**Example 1:**
```
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
```

**Example 2:**
```
Input: s = "aabcbaa"
Output: 17
```

**Constraints:**
- 1 <= s.length <= 500
- s consists of only lowercase English letters.

<details><summary>Hints</summary>

1. Maintain a prefix sum for the frequencies of characters.
2. You can iterate over all substring then iterate over the alphabet and find which character appears most and which appears least using the prefix sum array

</details>
