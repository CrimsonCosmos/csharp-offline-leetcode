# 3306. Count of Substrings Containing Every Vowel and K Consonants II
**Difficulty:** Medium  
**Topics:** Hash Table, String, Sliding Window
**Link (online only):** https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

**Example 1:**
```
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.
```

**Example 2:**
```
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4] , which is "aeiou" .
```

**Example 3:**
```
Input: word = " ieaouqqieaouqq ", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
```

**Constraints:**
- 5 <= word.length <= 2 * 105
- word consists only of lowercase English letters.
- 0 <= k <= word.length - 5

<details><summary>Hints</summary>

1. We can use sliding window and binary search.
2. For each index <code>r</code>, find the maximum <code>l</code> such that both conditions are satisfied using binary search.

</details>
