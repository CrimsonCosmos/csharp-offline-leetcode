# 1993. Operations on Tree
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Design
**Link (online only):** https://leetcode.com/problems/operations-on-tree/

You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.
The data structure should support the following functions:
Implement the LockingTree class:

**Example 1:**
```
Input
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output
[null, true, false, true, true, true, false]

Explanation
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.
```

**Constraints:**
- n == parent.length
- 2 <= n <= 2000
- 0 <= parent[i] <= n - 1 for i != 0
- parent[0] == -1
- 0 <= num <= n - 1
- 1 <= user <= 104
- parent represents a valid tree.
- At most 2000 calls in total will be made to lock, unlock, and upgrade.

<details><summary>Hints</summary>

1. How can we use the small constraints to help us solve the problem?
2. How can we traverse the ancestors and descendants of a node?

</details>
