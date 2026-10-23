# 606. Construct String from Binary Tree
**Difficulty:** Medium  
**Topics:** String, Tree, Depth-First Search, Binary Tree
**Link (online only):** https://leetcode.com/problems/construct-string-from-binary-tree/

Given the root node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:

**Example 1:**
```
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the empty parenthesis pairs. And it will be "1(2(4))(3)".
```

**Example 2:**
```
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except the () after 2 is necessary to indicate the absence of a left child for 2 and the presence of a right child.
```

**Constraints:**
- The number of nodes in the tree is in the range [1, 104].
- -1000 <= Node.val <= 1000

