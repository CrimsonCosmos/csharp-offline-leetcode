# 655. Print Binary Tree
**Difficulty:** Medium  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link (online only):** https://leetcode.com/problems/print-binary-tree/

Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:
Return the constructed matrix res.

**Example 1:**
```
Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
```

**Example 2:**
```
Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
```

**Constraints:**
- The number of nodes in the tree is in the range [1, 210].
- -99 <= Node.val <= 99
- The depth of the tree will be in the range [1, 10].

