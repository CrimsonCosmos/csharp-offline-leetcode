# 3332. Maximum Points Tourist Can Earn
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Matrix
**Link (online only):** https://leetcode.com/problems/maximum-points-tourist-can-earn/

You are given two integers, n and k, along with two 2D integer arrays, stayScore and travelScore.
A tourist is visiting a country with n cities, where each city is directly connected to every other city. The tourist's journey consists of exactly k 0-indexed days, and they can choose any city as their starting point.
Each day, the tourist has two choices:
Return the maximum possible points the tourist can earn.

**Example 1:**
```
Input: n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]]
Output: 3
Explanation:
The tourist earns the maximum number of points by starting in city 1 and staying in that city.
```

**Example 2:**
```
Input: n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]]
Output: 8
Explanation:
The tourist earns the maximum number of points by starting in city 1, staying in that city on day 0, and traveling to city 2 on day 1.
```

**Constraints:**
- 1 <= n <= 200
- 1 <= k <= 200
- n == travelScore.length == travelScore[i].length == stayScore[i].length
- k == stayScore.length
- 1 <= stayScore[i][j] <= 100
- 0 <= travelScore[i][j] <= 100
- travelScore[i][i] == 0

<details><summary>Hints</summary>

1. Use DP.
2. <code>dp[i][j]</code> is the maximum score that you can achieve in your last <code>i</code> actions by starting from city <code>j</code>.

</details>
