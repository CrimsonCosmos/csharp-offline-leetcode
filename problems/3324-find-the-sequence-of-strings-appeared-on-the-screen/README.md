# 3324. Find the Sequence of Strings Appeared on the Screen
**Difficulty:** Medium  
**Topics:** String, Simulation
**Link (online only):** https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

You are given a string target.
Alice is going to type target on her computer using a special keyboard that has only two keys:
Note that initially there is an empty string "" on the screen, so she can only press key 1.
Return a list of all strings that appear on the screen as Alice types target, in the order they appear, using the minimum key presses.

**Example 1:**
```
Input: target = "abc"
Output: ["a","aa","ab","aba","abb","abc"]
Explanation:
The sequence of key presses done by Alice are:
```

**Example 2:**
```
Input: target = "he"
Output: ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
```

**Constraints:**
- 1 <= target.length <= 400
- target consists only of lowercase English letters.

<details><summary>Hints</summary>

1. Append the character <code>'a'</code> using key 1.
2. Convert it to the required character using key 2.

</details>
