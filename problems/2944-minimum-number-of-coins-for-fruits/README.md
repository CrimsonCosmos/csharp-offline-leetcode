# 2944. Minimum Number of Coins for Fruits
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue
**Link (online only):** https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

You are given an 0-indexed integer array prices where prices[i] denotes the number of coins needed to purchase the (i + 1)th fruit.
The fruit market has the following reward for each fruit:
Note that even if you can take fruit j for free, you can still purchase it for prices[j - 1] coins to receive its reward.
Return the minimum number of coins needed to acquire all the fruits.

**Example 1:**
```
Input: prices = [3,1,2]
Output: 4
Explanation:
Note that even though you could take the 2 nd fruit for free as a reward of buying 1 st fruit, you purchase it to receive its reward, which is more optimal.
```

**Example 2:**
```
Input: prices = [1,10,1,1]
Output: 2
Explanation:
```

**Example 3:**
```
Input: prices = [26,18,6,12,49,7,45,45]
Output: 39
Explanation:
Note that even though you could take the 6 th fruit for free as a reward of buying 3 rd fruit, you purchase it to receive its reward, which is more optimal.
```

**Constraints:**
- 1 <= prices.length <= 1000
- 1 <= prices[i] <= 105

<details><summary>Hints</summary>

1. The intended solution uses Dynamic Programming.
2. Let <code>dp[i]</code> denote the minimum number of coins, such that we bought <code>i<sup>th</sup></code> fruit and acquired all the fruits in the range <code>[i...n]</code>.
3. <code>dp[i] = min(dp[i], dp[j] + prices[i]) </code>, where <code>j</code> is in the range <code>[i + 1, i + 1 + i]</code>.

</details>
