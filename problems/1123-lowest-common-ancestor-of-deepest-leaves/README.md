# 1123. Lowest Common Ancestor of Deepest Leaves
**Difficulty:** Medium  
**Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link (online only):** https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
Recall that:
Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
```

**Example 2:**
```
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.
```

**Example 3:**
```
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
```

**Constraints:**
- The number of nodes in the tree will be in the range [1, 1000].
- 0 <= Node.val <= 1000
- The values of the nodes in the tree are unique.

<details><summary>Hints</summary>

1. Do a postorder traversal.
2. Then, if both subtrees contain a deepest leaf, you can mark this node as the answer (so far).
3. The final node marked will be the correct answer.

</details>
