# 3618. Split Array by Prime Indices
**Difficulty:** Medium  
**Topics:** Array, Math, Number Theory
**Link (online only):** https://leetcode.com/problems/split-array-by-prime-indices/

You are given an integer array nums.
Split nums into two arrays A and B using the following rule:
Return the absolute difference between the sums of the two arrays: |sum(A) - sum(B)|.
Note: An empty array has a sum of 0.

**Example 1:**
```
Input: nums = [2,3,4]
Output: 1
Explanation:
```

**Example 2:**
```
Input: nums = [-1,5,7,0]
Output: 3
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Generate all primes up to <code>nums.length</code> (e.g., with the Sieve of Eratosthenes).
2. Iterate through <code>nums</code>, adding <code>nums[i]</code> to <code>sumA</code> if <code>i</code> is prime, otherwise to <code>sumB</code>, then return <code>|sumA - sumB|</code>.

</details>
