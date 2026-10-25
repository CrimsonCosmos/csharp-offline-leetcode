# 3457. Eat Pizzas!
**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/eat-pizzas/

You are given an integer array pizzas of size n, where pizzas[i] represents the weight of the ith pizza. Every day, you eat exactly 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights W, X, Y, and Z, where W <= X <= Y <= Z, you gain the weight of only 1 pizza!
Find the maximum total weight you can gain by eating all pizzas optimally.
Note: It is guaranteed that n is a multiple of 4, and each pizza can be eaten only once.

**Example 1:**
```
Input: pizzas = [1,2,3,4,5,6,7,8]
Output: 14
Explanation:
The total weight gained after eating all the pizzas is 8 + 6 = 14 .
```

**Example 2:**
```
Input: pizzas = [2,1,1,1,1,1,1,1]
Output: 3
Explanation:
The total weight gained after eating all the pizzas is 2 + 1 = 3.
```

**Constraints:**
- 4 <= n == pizzas.length <= 2 * 105
- 1 <= pizzas[i] <= 105
- n is a multiple of 4.

<details><summary>Hints</summary>

1. On odd-numbered days, it is optimal to pair the smallest three and the largest one.
2. On even-numbered days, it is optimal to pair the smallest two and the largest two.
3. There will be ceil((n / 4) / 2) odd-numbered days. Select pizzas for all odd-numbered days first.
4. Select the remaining pizzas for the even-numbered days.

</details>
