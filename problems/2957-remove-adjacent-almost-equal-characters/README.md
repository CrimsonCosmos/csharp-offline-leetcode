# 2957. Remove Adjacent Almost-Equal Characters
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.

**Example 1:**
```
Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
```

**Example 2:**
```
Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
```

**Example 3:**
```
Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.
```

**Constraints:**
- 1 <= word.length <= 100
- word consists only of lowercase English letters.

<details><summary>Hints</summary>

1. For <code>i > 0</code>, if <code>word[i]</code> and <code>word[i - 1]</code> are adjacent, we will change <code>word[i]</code> to another character. Which character should we change it to?
2. We will change <code>word[i]</code> to some character that is not adjacent to <code>word[i - 1]</code> nor <code>word[i + 1]</code> (if it exists). Such a character always exists. However, since the problem does not ask for the final state of the string, It is enough to prove that the character exists and we do not need to find it.

</details>
