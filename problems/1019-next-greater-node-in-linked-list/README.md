# 1019. Next Greater Node In Linked List
**Difficulty:** Medium  
**Topics:** Array, Linked List, Stack, Monotonic Stack
**Link (online only):** https://leetcode.com/problems/next-greater-node-in-linked-list/

You are given the head of a linked list with n nodes.
For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

**Example 1:**
```
Input: head = [2,1,5]
Output: [5,5,0]
```

**Example 2:**
```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Constraints:**
- The number of nodes in the list is n.
- 1 <= n <= 104
- 1 <= Node.val <= 109

<details><summary>Hints</summary>

1. We can use a stack that stores nodes in monotone decreasing order of value.  When we see a node_j with a larger value, every node_i in the stack has next_larger(node_i) = node_j .

</details>
