# 2266. Count Number of Texts
**Difficulty:** Medium  
**Topics:** Hash Table, Math, String, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/count-number-of-texts/

Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.
In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.
Since the answer may be very large, return it modulo 109 + 7.

**Example 1:**
```
Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
```

**Example 2:**
```
Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.
```

**Constraints:**
- 1 <= pressedKeys.length <= 105
- pressedKeys only consists of digits from '2' - '9'.

<details><summary>Hints</summary>

1. For a substring consisting of the same digit, how can we count the number of texts it could have originally represented?
2. How can dynamic programming help us calculate the required answer?

</details>
