# 3227. Vowels Game in a String
**Difficulty:** Medium  
**Topics:** Math, String, Brainteaser, Game Theory
**Link (online only):** https://leetcode.com/problems/vowels-game-in-a-string/

Alice and Bob are playing a game on a string.
You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:
The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.
Return true if Alice wins the game, and false otherwise.
The English vowels are: a, e, i, o, and u.

**Example 1:**
```
Input: s = "leetcoder"
Output: true
Explanation: Alice can win the game as follows:
```

**Example 2:**
```
Input: s = "bbcd"
Output: false
Explanation: There is no valid play for Alice in her first turn, so Alice loses the game.
```

**Constraints:**
- 1 <= s.length <= 105
- s consists only of lowercase English letters.

<details><summary>Hints</summary>

1. If there are no vowels in the initial string, then Bob wins.
2. If the number of vowels in the initial string is odd, then Alice can remove the whole string on her first turn and win.
3. What if the number of vowels in the initial string is even? What’s the optimal play for Alice’s first turn?

</details>
