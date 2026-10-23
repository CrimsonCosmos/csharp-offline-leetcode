# 729. My Calendar I
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Design, Segment Tree, Ordered Set
**Link (online only):** https://leetcode.com/problems/my-calendar-i/

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
Implement the MyCalendar class:

**Example 1:**
```
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

**Constraints:**
- 0 <= start < end <= 109
- At most 1000 calls will be made to book.

<details><summary>Hints</summary>

1. Store the events as a sorted list of intervals.  If none of the events conflict, then the new event can be added.

</details>
