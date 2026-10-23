# 1888. Minimum Number of Flips to Make the Binary String Alternating
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Sliding Window
**Link (online only):** https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.

**Example 1:**
```
Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
```

**Example 2:**
```
Input: s = "010"
Output: 0
Explanation: The string is already alternating.
```

**Example 3:**
```
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
```

**Constraints:**
- 1 <= s.length <= 105
- s[i] is either '0' or '1'.

<details><summary>Hints</summary>

1. Note what actually matters is how many 0s and 1s are in odd and even positions
2. For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity

</details>
