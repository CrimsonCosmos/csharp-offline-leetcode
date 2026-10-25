# 1750. Minimum Length of String After Deleting Similar Ends
**Difficulty:** Medium  
**Topics:** Two Pointers, String
**Link (online only):** https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

**Example 1:**
```
Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
```

**Example 2:**
```
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
```

**Example 3:**
```
Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
```

**Constraints:**
- 1 <= s.length <= 105
- s only consists of characters 'a', 'b', and 'c'.

<details><summary>Hints</summary>

1. If both ends have distinct characters, no more operations can be made. Otherwise, the only operation is to remove all of the same characters from both ends. We will do this as many times as we can.
2. Note that if the length is equal 1 the answer is 1

</details>
