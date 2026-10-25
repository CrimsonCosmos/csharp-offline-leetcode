# 2901. Longest Unequal Adjacent Groups Subsequence II
**Difficulty:** Medium  
**Topics:** Array, String, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

You are given a string array words, and an array groups, both arrays having length n.
The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.
You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.
Note: strings in words may be unequal in length.

**Example 1:**
```
Input: words = ["bab","dab","cab"], groups = [1,2,2]
Output: ["bab","cab"]
Explanation: A subsequence that can be selected is [0,2] .
So, a valid answer is [words[0],words[2]] = ["bab","cab"] .
Another subsequence that can be selected is [0,1] .
So, another valid answer is [words[0],words[1]] = ["bab","dab"] .
It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2 .
```

**Example 2:**
```
Input: words = ["a","b","c","d"], groups = [1,2,3,4]
Output: ["a","b","c","d"]
Explanation: We can select the subsequence [0,1,2,3] .
It satisfies both conditions.
Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"] .
It has the longest length among all subsequences of indices that satisfy the conditions.
Hence, it is the only answer.
```

**Constraints:**
- 1 <= n == words.length == groups.length <= 1000
- 1 <= words[i].length <= 10
- 1 <= groups[i] <= n
- words consists of distinct strings.
- words[i] consists of lowercase English letters.

<details><summary>Hints</summary>

1. Let <code>dp[i]</code> represent the length of the longest subsequence ending with <code>words[i]</code> that satisfies the conditions.
2. <code>dp[i] =</code> (maximum value of <code>dp[j]</code>) <code>+ 1</code> for indices <code>j < i</code>, where <code>groups[i] != groups[j]</code>, <code>words[i]</code> and <code>words[j]</code> are equal in length, and the hamming distance between <code>words[i]</code> and <code>words[j]</code> is exactly <code>1</code>.
3. Keep track of the <code>j</code> values used to achieve the maximum <code>dp[i]</code> for each index <code>i</code>.
4. The expected array's length is <code>max(dp[0:n])</code>, and starting from the index having the maximum value in <code>dp</code>, we can trace backward to get the words.

</details>
