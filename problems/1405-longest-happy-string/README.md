# 1405. Longest Happy String
**Difficulty:** Medium  
**Topics:** String, Greedy, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/longest-happy-string/

A string s is called happy if it satisfies the following conditions:
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
A substring is a contiguous sequence of characters within a string.

**Example 1:**
```
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

**Example 2:**
```
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
```

**Constraints:**
- 0 <= a, b, c <= 100
- a + b + c > 0

<details><summary>Hints</summary>

1. Use a greedy approach.
2. Use the letter with the maximum current limit that can be added without breaking the condition.

</details>
