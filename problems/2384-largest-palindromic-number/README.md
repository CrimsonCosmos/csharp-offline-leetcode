# 2384. Largest Palindromic Number
**Difficulty:** Medium  
**Topics:** Hash Table, String, Greedy, Counting
**Link (online only):** https://leetcode.com/problems/largest-palindromic-number/

You are given a string num consisting of digits only.
Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.
Notes:

**Example 1:**
```
Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
```

**Example 2:**
```
Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
```

**Constraints:**
- 1 <= num.length <= 105
- num consists of digits.

<details><summary>Hints</summary>

1. In order to form a valid palindrome, other than the middle digit in an odd-length palindrome, every digit needs to exist on both sides.
2. A longer palindrome implies a larger valued palindrome. For palindromes of the same length, the larger digits should occur first.
3. We can count the occurrences of each digit and build the palindrome starting from the ends. Starting from the larger digits, if there are still at least 2 occurrences of a digit, we can place these digits on each side.
4. Make sure to consider the special case for the center digit (if any) and zeroes. There should not be leading zeroes.

</details>
