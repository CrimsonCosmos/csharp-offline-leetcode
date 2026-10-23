# 2672. Number of Adjacent Elements With the Same Color
**Difficulty:** Medium  
**Topics:** Array
**Link (online only):** https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:
Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

**Example 1:**
```
Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
Output: [0,1,1,0,2]
Explanation:
```

**Example 2:**
```
Input: n = 1, queries = [[0,100000]]
Output: [0]
Explanation:
After the 1 st query colors = [100000]. The count of adjacent pairs with the same color is 0.
```

**Constraints:**
- 1 <= n <= 105
- 1 <= queries.length <= 105
- queries[i].length == 2
- 0 <= indexi <= n - 1
- 1 <=  colori <= 105

<details><summary>Hints</summary>

1. Since at each query, only one element is being recolored, we just need to focus on its neighbors.
2. If an element that is changed on the i-th query had the same color as its right element answer decreases by 1. Similarly contributes its left element too.
3. After changing the color, if the element has the same color as its right element answer increases by 1. Similarly contributes its left element too.

</details>
