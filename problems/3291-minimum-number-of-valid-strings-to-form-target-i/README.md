# 3291. Minimum Number of Valid Strings to Form Target I
**Difficulty:** Medium  
**Topics:** Array, String, Binary Search, Dynamic Programming, Trie, Segment Tree, Rolling Hash, String Matching, Hash Function
**Link (online only):** https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

You are given an array of strings words and a string target.
A string x is called valid if x is a prefix of any string in words.
Return the minimum number of valid strings that can be concatenated to form target. If it is not possible to form target, return -1.

**Example 1:**
```
Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
Output: 3
Explanation:
The target string can be formed by concatenating:
```

**Example 2:**
```
Input: words = ["abababab","ab"], target = "ababaababa"
Output: 2
Explanation:
The target string can be formed by concatenating:
```

**Example 3:**
```
Input: words = ["abcdef"], target = "xyz"
Output: -1
```

**Constraints:**
- 1 <= words.length <= 100
- 1 <= words[i].length <= 5 * 103
- The input is generated such that sum(words[i].length) <= 105.
- words[i] consists only of lowercase English letters.
- 1 <= target.length <= 5 * 103
- target consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Let <code>dp[i]</code> be the minimum cost to form the prefix of length <code>i</code> of <code>target</code>.
2. If <code>target[(i + 1)..j]</code> matches any prefix, update the range <code>dp[(i + 1)..j]</code> to minimum between original value and <code>dp[i] + 1</code>.
3. Use a Trie to check prefix matching.

</details>
