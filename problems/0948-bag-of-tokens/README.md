# 948. Bag of Tokens
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/bag-of-tokens/

You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.
Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
Return the maximum possible score you can achieve after playing any number of tokens.

**Example 1:**
```
Input: tokens = [100], power = 50
Output: 0
Explanation : Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power ( 50 ) is less than tokens[0] ( 100 ).
```

**Example 2:**
```
Input: tokens = [200,100], power = 150
Output: 1
Explanation: Play token 1 ( 100 ) face-up, reducing your power to 50 and increasing your score to 1 .
There is no need to play token 0 , since you cannot play it face-up to add to your score. The maximum score achievable is 1 .
```

**Example 3:**
```
Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2 :
The maximum score achievable is 2 .
```

**Constraints:**
- 0 <= tokens.length <= 1000
- 0 <= tokens[i], power < 104

