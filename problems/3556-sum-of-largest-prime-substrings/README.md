# 3556. Sum of Largest Prime Substrings
**Difficulty:** Medium  
**Topics:** Hash Table, Math, String, Sorting, Number Theory
**Link (online only):** https://leetcode.com/problems/sum-of-largest-prime-substrings/

Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.
Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.
Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

**Example 1:**
```
Input: s = "12234"
Output: 1469
Explanation:
```

**Example 2:**
```
Input: s = "111"
Output: 11
Explanation:
```

**Constraints:**
- 1 <= s.length <= 10
- s consists of only digits.

<details><summary>Hints</summary>

1. Iterate over all substrings of <code>s</code> to generate candidate numbers.
2. Check each candidate for primality in <code>O(sqrt(n))</code> time.
3. Store unique primes, then sum the three largest (or all if fewer than three).

</details>
