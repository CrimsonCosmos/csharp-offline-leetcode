# 2606. Find the Substring With Maximum Cost
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/find-the-substring-with-maximum-cost/

You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.
The cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.
The value of the character is defined in the following way:
Return the maximum cost among all substrings of the string s.

**Example 1:**
```
Input: s = "adaa", chars = "d", vals = [-1000]
Output: 2
Explanation: The value of the characters "a" and "d" is 1 and -1000 respectively.
The substring with the maximum cost is "aa" and its cost is 1 + 1 = 2.
It can be proven that 2 is the maximum cost.
```

**Example 2:**
```
Input: s = "abc", chars = "abc", vals = [-1,-1,-1]
Output: 0
Explanation: The value of the characters "a", "b" and "c" is -1, -1, and -1 respectively.
The substring with the maximum cost is the empty substring "" and its cost is 0.
It can be proven that 0 is the maximum cost.
```

**Constraints:**
- 1 <= s.length <= 105
- s consist of lowercase English letters.
- 1 <= chars.length <= 26
- chars consist of distinct lowercase English letters.
- vals.length == chars.length
- -1000 <= vals[i] <= 1000

<details><summary>Hints</summary>

1. Create a new integer array where arr[i] denotes the value of character s[i].
2. We can use Kadane’s maximum subarray sum algorithm to find the maximum cost.

</details>
