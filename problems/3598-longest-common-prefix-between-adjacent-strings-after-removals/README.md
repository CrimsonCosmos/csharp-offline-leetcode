# 3598. Longest Common Prefix Between Adjacent Strings After Removals
**Difficulty:** Medium  
**Topics:** Array, String
**Link (online only):** https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

**Example 1:**
```
Input: words = ["jump","run","run","jump","run"]
Output: [3,0,0,3,3]
Explanation:
```

**Example 2:**
```
Input: words = ["dog","racer","car"]
Output: [0,0,0]
Explanation:
```

**Constraints:**
- 1 <= words.length <= 105
- 1 <= words[i].length <= 104
- words[i] consists of lowercase English letters.
- The sum of words[i].length is smaller than or equal 105.

<details><summary>Hints</summary>

1. Precompute the longest common prefix length for adjacent prefixes and suffixes.
2. After deleting <code>words[i]</code>, compute the longest common prefix for <code>words[i - 1]</code> and <code>words[i + 1]</code> (if they exist).
3. Use the result of the prefix computation up to <code>i - 1</code> and the suffix computation from <code>i + 1</code> onwards.

</details>
