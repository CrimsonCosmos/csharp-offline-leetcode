# 3628. Maximum Number of Subsequences After One Inserting
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

You are given a string s consisting of uppercase English letters.
You are allowed to insert at most one uppercase English letter at any position (including the beginning or end) of the string.
Return the maximum number of "LCT" subsequences that can be formed in the resulting string after at most one insertion.

**Example 1:**
```
Input: s = "LMCT"
Output: 2
Explanation:
We can insert a "L" at the beginning of the string s to make "LLMCT" , which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].
```

**Example 2:**
```
Input: s = "LCCT"
Output: 4
Explanation:
We can insert a "L" at the beginning of the string s to make "LLCCT" , which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].
```

**Example 3:**
```
Input: s = "L"
Output: 0
Explanation:
Since it is not possible to obtain the subsequence "LCT" by inserting a single letter, the result is 0.
```

**Constraints:**
- 1 <= s.length <= 105
- s consists of uppercase English letters.

<details><summary>Hints</summary>

1. Precompute <code>preL</code>, <code>preLC</code>, <code>sufT</code>, and <code>sufCT</code> arrays to count L’s, LC’s, T’s, and CT’s at each position.
2. Compute <code>base</code> as the sum over all i of <code>preLC[i] * sufT[i]</code>.
3. For each insert position i, compute gains <code>sufCT[i]</code> for ‘L’, <code>preL[i] * sufT[i]</code> for ‘C’, and <code>preLC[i]</code> for ‘T’, and take the maximum of <code>base</code> and <code>base + gain</code>.

</details>
