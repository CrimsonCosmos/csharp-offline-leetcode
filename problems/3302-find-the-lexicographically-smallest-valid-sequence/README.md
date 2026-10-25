# 3302. Find the Lexicographically Smallest Valid Sequence
**Difficulty:** Medium  
**Topics:** Two Pointers, String, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

You are given two strings word1 and word2.
A string x is called almost equal to y if you can change at most one character in x to make it identical to y.
A sequence of indices seq is called valid if:
Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.
Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

**Example 1:**
```
Input: word1 = "vbcca", word2 = "abc"
Output: [0,1,2]
Explanation:
The lexicographically smallest valid sequence of indices is [0, 1, 2] :
```

**Example 2:**
```
Input: word1 = "bacdc", word2 = "abc"
Output: [1,2,4]
Explanation:
The lexicographically smallest valid sequence of indices is [1, 2, 4] :
```

**Example 3:**
```
Input: word1 = "aaaaaa", word2 = "aaabc"
Output: []
Explanation:
There is no valid sequence of indices.
```

**Example 4:**
```
Input: word1 = "abc", word2 = "ab"
Output: [0,1]
```

**Constraints:**
- 1 <= word2.length < word1.length <= 3 * 105
- word1 and word2 consist only of lowercase English letters.

<details><summary>Hints</summary>

1. Let <code>dp[i]</code> be the longest suffix of <code>word2</code> that exists as a subsequence of suffix of the substring of <code>word1</code> starting at index <code>i</code>.
2. If <code>dp[i + 1] < m</code> and <code>word1[i] == word2[m - dp[i + 1] - 1]</code>,<code>dp[i] =  dp[i + 1] + 1</code>. Otherwise, <code>dp[i] =  dp[i + 1]</code>.
3. For each index <code>i</code>, greedily select characters using the <code>dp</code> array to know whether a solution exists.

</details>
