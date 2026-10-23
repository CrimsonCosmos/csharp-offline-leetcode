# 3479. Fruits Into Baskets III
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Segment Tree, Ordered Set
**Link (online only):** https://leetcode.com/problems/fruits-into-baskets-iii/

You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
From left to right, place the fruits according to these rules:
Return the number of fruit types that remain unplaced after all possible allocations are made.

**Example 1:**
```
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
Since one fruit type remains unplaced, we return 1.
```

**Example 2:**
```
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:
Since all fruits are successfully placed, we return 0.
```

**Constraints:**
- n == fruits.length == baskets.length
- 1 <= n <= 105
- 1 <= fruits[i], baskets[i] <= 109

<details><summary>Hints</summary>

1. Sort the baskets by the pair of <code>(basket[i], i)</code> in the array.
2. For each fruit from left to right, use binary search to find the first index in the sorted array such that <code>basket[i] >= fruit</code>.
3. Use a segment tree to maintain the smallest original indices where <code>basket[i] >= fruit</code>.
4. When a valid index is found, set the corresponding point to infinity to mark it as used.

</details>
