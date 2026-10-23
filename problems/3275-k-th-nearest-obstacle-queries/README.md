# 3275. K-th Nearest Obstacle Queries
**Difficulty:** Medium  
**Topics:** Array, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/k-th-nearest-obstacle-queries/

There is an infinite 2D plane.
You are given a positive integer k. You are also given a 2D array queries, which contains the following queries:
After each query, you need to find the distance of the kth nearest obstacle from the origin.
Return an integer array results where results[i] denotes the kth nearest obstacle after query i, or results[i] == -1 if there are less than k obstacles.
Note that initially there are no obstacles anywhere.
The distance of an obstacle at coordinate (x, y) from the origin is given by |x| + |y|.

**Example 1:**
```
Input: queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2
Output: [-1,7,5,3]
Explanation:
```

**Example 2:**
```
Input: queries = [[5,5],[4,4],[3,3]], k = 1
Output: [10,8,6]
Explanation:
```

**Constraints:**
- 1 <= queries.length <= 2 * 105
- All queries[i] are unique.
- -109 <= queries[i][0], queries[i][1] <= 109
- 1 <= k <= 105

<details><summary>Hints</summary>

1. Consider if there are more than <code>k</code> obstacles. Can the <code>k + 1<sup>th</sup></code> obstacle ever be the answer to any query?
2. Maintain a max heap of size <code>k</code>, thus heap will contain minimum element at the top in that queue.
3. Remove top element and insert new element from input array if current max is larger than this.

</details>
