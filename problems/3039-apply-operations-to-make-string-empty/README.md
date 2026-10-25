# 3039. Apply Operations to Make String Empty
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Sorting, Counting
**Link (online only):** https://leetcode.com/problems/apply-operations-to-make-string-empty/

You are given a string s.
Consider performing the following operation until s becomes empty:
For example, let initially s = "aabcbbca". We do the following operations:
Return the value of the string s right before applying the last operation. In the example above, answer is "ba".

**Example 1:**
```
Input: s = "aabcbbca"
Output: "ba"
Explanation: Explained in the statement.
```

**Example 2:**
```
Input: s = "abcd"
Output: "abcd"
Explanation: We do the following operation:
- Remove the underlined characters s = "abcd". The resulting string is s = "".
The string just before the last operation is "abcd".
```

**Constraints:**
- 1 <= s.length <= 5 * 105
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Before the last operation, only the most frequent characters in the original string will remain.
2. Keep only the last occurence of each of the most frequent characters.

</details>
