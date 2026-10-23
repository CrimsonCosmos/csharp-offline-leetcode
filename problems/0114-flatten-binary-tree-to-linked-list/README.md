# 114. Flatten Binary Tree to Linked List
**Difficulty:** Medium  
**Topics:** Linked List, Stack, Tree, Depth-First Search, Binary Tree
**Link (online only):** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":

**Example 1:**
```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Example 2:**
```
Input: root = []
Output: []
```

**Example 3:**
```
Input: root = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

<details><summary>Hints</summary>

1. If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

</details>
