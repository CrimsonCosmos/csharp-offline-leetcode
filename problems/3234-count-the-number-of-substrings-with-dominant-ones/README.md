# 3234. Count the Number of Substrings With Dominant Ones
**Difficulty:** Medium  
**Topics:** String, Sliding Window, Enumeration
**Link (online only):** https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

You are given a binary string s.
Return the number of substrings with dominant ones.
A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

**Example 1:**
```
Input: s = "00011"
Output: 5
Explanation:
The substrings with dominant ones are shown in the table below.
```

**Example 2:**
```
Input: s = "101101"
Output: 16
Explanation:
The substrings with non-dominant ones are shown in the table below.
Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
```

**Constraints:**
- 1 <= s.length <= 4 * 104
- s consists only of characters '0' and '1'.

<details><summary>Hints</summary>

1. Let us fix the starting index <code>l</code> of the substring and count the number of indices <code>r</code> such that <code>l <= r</code> and the substring <code>s[l..r]</code> has dominant ones.
2. A substring with dominant ones has at most <code>sqrt(n)</code> zeros.
3. We cannot iterate over every <code>r</code> and check if the  <code>s[l..r]</code> has dominant ones. Instead, we iterate over the next <code>sqrt(n)</code> zeros to the left of <code>l</code> and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

</details>
