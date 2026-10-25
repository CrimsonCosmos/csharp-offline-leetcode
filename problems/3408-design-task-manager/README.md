# 3408. Design Task Manager
**Difficulty:** Medium  
**Topics:** Hash Table, Design, Heap (Priority Queue), Ordered Set
**Link (online only):** https://leetcode.com/problems/design-task-manager/

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.
Implement the TaskManager class:
Note that a user may be assigned multiple tasks.

**Example 1:**
```
Input: ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"] [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
Output: [null, null, null, 3, null, null, 5]
Explanation
```

**Constraints:**
- 1 <= tasks.length <= 105
- 0 <= userId <= 105
- 0 <= taskId <= 105
- 0 <= priority <= 109
- 0 <= newPriority <= 109
- At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
- The input is generated such that taskId will be valid.

