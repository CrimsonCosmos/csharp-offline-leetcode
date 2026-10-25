# 3180. Maximum Total Reward Using Operations I
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/maximum-total-reward-using-operations-i/

You are given an integer array rewardValues of length n, representing the values of rewards.
Initially, your total reward x is 0, and all indices are unmarked. You are allowed to perform the following operation any number of times:
Return an integer denoting the maximum total reward you can collect by performing the operations optimally.

**Example 1:**
```
Input: rewardValues = [1,1,3,3]
Output: 4
Explanation:
During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.
```

**Example 2:**
```
Input: rewardValues = [1,6,4,3,2]
Output: 11
Explanation:
Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.
```

**Constraints:**
- 1 <= rewardValues.length <= 2000
- 1 <= rewardValues[i] <= 2000

<details><summary>Hints</summary>

1. Sort the rewards array first.
2. If we decide to apply some rewards, it's always optimal to apply them in order.
3. Let <code>dp[i][j]</code> (true/false) be the state after the first <code>i</code> rewards, indicating whether we can get exactly <code>j</code> points.
4. The transition is given by: <code>dp[i][j] = dp[i - 1][j − rewardValues[i]]</code> if <code>j − rewardValues[i] < rewardValues[i]</code>.

</details>
