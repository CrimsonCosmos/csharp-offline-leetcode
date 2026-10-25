# 1845. Seat Reservation Manager
**Difficulty:** Medium  
**Topics:** Design, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/seat-reservation-manager/

Design a system that manages the reservation state of n seats that are numbered from 1 to n.
Implement the SeatManager class:

**Example 1:**
```
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
```

**Constraints:**
- 1 <= n <= 105
- 1 <= seatNumber <= n
- For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
- For each call to unreserve, it is guaranteed that seatNumber will be reserved.
- At most 105 calls in total will be made to reserve and unreserve.

<details><summary>Hints</summary>

1. You need a data structure that maintains the states of the seats. This data structure should also allow you to get the first available seat and flip the state of a seat in a reasonable time.
2. You can let the data structure contain the available seats. Then you want to be able to get the lowest element and erase an element, in a reasonable time.
3. Ordered sets support these operations.

</details>
