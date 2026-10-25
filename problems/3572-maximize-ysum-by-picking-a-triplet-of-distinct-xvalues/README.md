# 3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:
Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.
If no such triplet exists, return -1.

**Example 1:**
```
Input: x = [1,2,1,3,2], y = [5,3,4,6,2]
Output: 14
Explanation:
```

**Example 2:**
```
Input: x = [1,2,1,2], y = [4,5,6,7]
Output: -1
Explanation:
```

**Constraints:**
- n == x.length == y.length
- 3 <= n <= 105
- 1 <= x[i], y[i] <= 106

<details><summary>Hints</summary>

1. For each unique <code>x</code>, keep only the maximum <code>y</code>; all other pairs with the same <code>x</code> are redundant.
2. Sort the pairs by <code>x</code> so that identical <code>x</code> values form contiguous blocks, then take the maximum <code>y</code> from each block.
3. Alternatively, use a map (or dictionary) from <code>x</code> to its largest <code>y</code>.

</details>
