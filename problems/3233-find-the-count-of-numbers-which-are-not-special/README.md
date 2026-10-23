# 3233. Find the Count of Numbers Which Are Not Special
**Difficulty:** Medium  
**Topics:** Array, Math, Number Theory
**Link (online only):** https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper divisors of x.
A number is called special if it has exactly 2 proper divisors. For example:
Return the count of numbers in the range [l, r] that are not special.

**Example 1:**
```
Input: l = 5, r = 7
Output: 3
Explanation:
There are no special numbers in the range [5, 7] .
```

**Example 2:**
```
Input: l = 4, r = 16
Output: 11
Explanation:
The special numbers in the range [4, 16] are 4 and 9.
```

**Constraints:**
- 1 <= l <= r <= 109

<details><summary>Hints</summary>

1. A special number must be a square of a prime number.
2. We need to find all primes in the range <code>[sqrt(l), sqrt(r)]</code>.
3. Use sieve to find primes till <code>sqrt(10<sup>9</sup>)</code>.

</details>
