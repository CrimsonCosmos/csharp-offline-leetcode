# 1054. Distant Barcodes
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
**Link (online only):** https://leetcode.com/problems/distant-barcodes/

In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

**Example 1:**
```
Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
```

**Example 2:**
```
Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
```

**Constraints:**
- 1 <= barcodes.length <= 10000
- 1 <= barcodes[i] <= 10000

<details><summary>Hints</summary>

1. We want to always choose the most common or second most common element to write next.  What data structure allows us to query this effectively?

</details>
