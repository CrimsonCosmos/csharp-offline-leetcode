# 3573. Best Time to Buy and Sell Stock V
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.
You are allowed to make at most k transactions, where each transaction can be either of the following:
Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.
Return the maximum total profit you can earn by making at most k transactions.

**Example 1:**
```
Input: prices = [1,7,9,8,2], k = 2
Output: 14
Explanation:
```

**Example 2:**
```
Input: prices = [12,16,19,19,8,1,19,13,9], k = 3
Output: 36
Explanation:
```

**Constraints:**
- 2 <= prices.length <= 103
- 1 <= prices[i] <= 109
- 1 <= k <= prices.length / 2

<details><summary>Hints</summary>

1. Use dynamic programming.
2. Keep the following states: <code>idx</code>, <code>transactionsDone</code>, <code>transactionType</code>, <code>isTransactionRunning</code>.
3. Transactions transition from completed -> running and from running -> completed.

</details>
