# 3472. Longest Palindromic Subsequence After at Most K Operations
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

You are given a string s and an integer k.
In one operation, you can replace the character at any position with the next or previous letter in the alphabet (wrapping around so that 'a' is after 'z'). For example, replacing 'a' with the next letter results in 'b', and replacing 'a' with the previous letter results in 'z'. Similarly, replacing 'z' with the next letter results in 'a', and replacing 'z' with the previous letter results in 'y'.
Return the length of the longest palindromic subsequence of s that can be obtained after performing at most k operations.

**Example 1:**
```
Input: s = "abced", k = 2
Output: 3
Explanation:
The subsequence "ccc" forms a palindrome of length 3, which is the maximum.
```

**Example 2:**
```
Input: s = " aaazzz ", k = 4
Output: 6
Explanation:
The entire string forms a palindrome of length 6.
```

**Constraints:**
- 1 <= s.length <= 200
- 1 <= k <= 200
- s consists of only lowercase English letters.

<details><summary>Hints</summary>

1. Use dynamic programming.
2. <code>dp[i][j][k]</code> is the length of the longest palindromic subsequence in substring <code>[i..j]</code> with cost at most <code>k</code>.
3. <code>dp[i][j][k] = max(dp[i + 1][j][k], dp[i][j - 1][k], dp[i + 1][j - 1][k - dist(s[i], s[j])] + 2)</code>, where <code>dist(x, y)</code> is the minimum cyclic distance between <code>x</code> and <code>y</code>.

</details>
