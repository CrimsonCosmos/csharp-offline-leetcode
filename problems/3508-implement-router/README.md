# 3508. Implement Router
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Binary Search, Design, Queue, Ordered Set
**Link (online only):** https://leetcode.com/problems/implement-router/

Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:
Implement the Router class:
Router(int memoryLimit): Initializes the Router object with a fixed memory limit.
bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.
int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.
int getCount(int destination, int startTime, int endTime):
Note that queries for addPacket will be made in increasing order of timestamp.

**Example 1:**
```
Input: ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"] [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
Output: [null, true, true, false, true, true, [2, 5, 90], true, 1]
Explanation
```

**Example 2:**
```
Input: ["Router", "addPacket", "forwardPacket", "forwardPacket"] [[2], [7, 4, 90], [], []]
Output: [null, true, [7, 4, 90], []]
Explanation
```

**Constraints:**
- 2 <= memoryLimit <= 105
- 1 <= source, destination <= 2 * 105
- 1 <= timestamp <= 109
- 1 <= startTime <= endTime <= 109
- At most 105 calls will be made to addPacket, forwardPacket, and getCount methods altogether.
- queries for addPacket will be made in increasing order of timestamp.

<details><summary>Hints</summary>

1. A deque can simulate the adding and forwarding of packets efficiently.
2. Use binary search for counting packets within a timestamp range.

</details>
