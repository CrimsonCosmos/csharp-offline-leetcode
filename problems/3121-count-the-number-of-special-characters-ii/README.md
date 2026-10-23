# 3121. Count the Number of Special Characters II
**Difficulty:** Medium  
**Topics:** Hash Table, String
**Link (online only):** https://leetcode.com/problems/count-the-number-of-special-characters-ii/

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.

**Example 1:**
```
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters are 'a' , 'b' , and 'c' .
```

**Example 2:**
```
Input: word = "abc"
Output: 0
Explanation:
There are no special characters in word .
```

**Example 3:**
```
Input: word = "AbBCab"
Output: 0
Explanation:
There are no special characters in word .
```

**Constraints:**
- 1 <= word.length <= 2 * 105
- word consists of only lowercase and uppercase English letters.

<details><summary>Hints</summary>

1. For each character <code>c</code>, store the first occurrence of its uppercase and the last occurrence of its lowercase.

</details>
