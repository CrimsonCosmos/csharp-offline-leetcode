# 1670. Design Front Middle Back Queue
**Difficulty:** Medium  
**Topics:** Array, Linked List, Design, Queue, Data Stream
**Link (online only):** https://leetcode.com/problems/design-front-middle-back-queue/

Design a queue that supports push and pop operations in the front, middle, and back.
Implement the FrontMiddleBack class:
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

**Example 1:**
```
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
```

**Constraints:**
- 1 <= val <= 109
- At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.

<details><summary>Hints</summary>

1. The constraints are low enough for a brute force, single array approach.
2. For an O(1) per method approach, use 2 double-ended queues: one for the first half and one for the second half.

</details>
