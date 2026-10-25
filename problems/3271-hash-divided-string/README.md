# 3271. Hash Divided String
**Difficulty:** Medium  
**Topics:** String, Simulation
**Link (online only):** https://leetcode.com/problems/hash-divided-string/

You are given a string s of length n and an integer k, where n is a multiple of k. Your task is to hash the string s into a new string called result, which has a length of n / k.
First, divide s into n / k substrings, each with a length of k. Then, initialize result as an empty string.
For each substring in order from the beginning:
Return result.

**Example 1:**
```
Input: s = "abcd", k = 2
Output: "bf"
Explanation:
First substring: "ab" , 0 + 1 = 1 , 1 % 26 = 1 , result[0] = 'b' .
Second substring: "cd" , 2 + 3 = 5 , 5 % 26 = 5 , result[1] = 'f' .
```

**Example 2:**
```
Input: s = "mxz", k = 3
Output: "i"
Explanation:
The only substring: "mxz" , 12 + 23 + 25 = 60 , 60 % 26 = 8 , result[0] = 'i' .
```

**Constraints:**
- 1 <= k <= 100
- k <= s.length <= 1000
- s.length is divisible by k.
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Try to find each substring.
2. Use a for loop to find <code>hashedChar</code> of each substring.
3. Find the answer using <code>hashedChar</code> of each substring.

</details>
