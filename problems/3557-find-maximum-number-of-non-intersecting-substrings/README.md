# 3557. Find Maximum Number of Non Intersecting Substrings
**Difficulty:** Medium  
**Topics:** Hash Table, String, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

You are given a string word.
Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.

**Example 1:**
```
Input: word = "abcdeafdef"
Output: 2
Explanation:
The two substrings are "abcdea" and "fdef" .
```

**Example 2:**
```
Input: word = "bcdaaaab"
Output: 1
Explanation:
The only substring is "aaaa" . Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.
```

**Constraints:**
- 1 <= word.length <= 2 * 105
- word consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Can we solve the problem using Dynamic Programming?
2. For each character <code>c</code>, store all occurrence indices in order
3. At each position <code>i</code>, let <code>j</code> be the first index of <code>word[i]</code>; if <code>i - j >= 3</code>, we can form substring <code>[j, i]</code>
4. For each index, also store the maximum for <b>any</b> substring ending before that index in the dp.

</details>
