# 1302. Deepest Leaves Sum
**Difficulty:** Medium  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link (online only):** https://leetcode.com/problems/deepest-leaves-sum/



**Example 1:**
```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```

**Example 2:**
```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
```

**Constraints:**
- The number of nodes in the tree is in the range [1, 104].
- 1 <= Node.val <= 100

<details><summary>Hints</summary>

1. Traverse the tree to find the max depth.
2. Traverse the tree again to compute the sum required.

</details>
