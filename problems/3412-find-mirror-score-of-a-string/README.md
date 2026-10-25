# 3412. Find Mirror Score of a String
**Difficulty:** Medium  
**Topics:** Hash Table, String, Stack, Simulation
**Link (online only):** https://leetcode.com/problems/find-mirror-score-of-a-string/

You are given a string s.
We define the mirror of a letter in the English alphabet as its corresponding letter when the alphabet is reversed. For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.
Initially, all characters in the string s are unmarked.
You start with a score of 0, and you perform the following process on the string s:
Return the total score at the end of the process.

**Example 1:**
```
Input: s = "aczzx"
Output: 5
Explanation:
```

**Example 2:**
```
Input: s = "abcdef"
Output: 0
Explanation:
For each index i , there is no index j that satisfies the conditions.
```

**Constraints:**
- 1 <= s.length <= 105
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Create a stack for every character.
2. For each index, check if the stack for mirror of the letter at that index is empty.

</details>
