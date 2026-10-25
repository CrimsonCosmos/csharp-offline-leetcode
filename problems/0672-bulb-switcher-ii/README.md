# 672. Bulb Switcher II
**Difficulty:** Medium  
**Topics:** Math, Bit Manipulation, Depth-First Search, Breadth-First Search
**Link (online only):** https://leetcode.com/problems/bulb-switcher-ii/

There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four buttons on the wall. Each of the four buttons has a different functionality where:
You must make exactly presses button presses in total. For each press, you may pick any of the four buttons to press.
Given the two integers n and presses, return the number of different possible statuses after performing all presses button presses.

**Example 1:**
```
Input: n = 1, presses = 1
Output: 2
Explanation: Status can be:
- [off] by pressing button 1
- [on] by pressing button 2
```

**Example 2:**
```
Input: n = 2, presses = 1
Output: 3
Explanation: Status can be:
- [off, off] by pressing button 1
- [on, off] by pressing button 2
- [off, on] by pressing button 3
```

**Example 3:**
```
Input: n = 3, presses = 1
Output: 4
Explanation: Status can be:
- [off, off, off] by pressing button 1
- [off, on, off] by pressing button 2
- [on, off, on] by pressing button 3
- [off, on, on] by pressing button 4
```

**Constraints:**
- 1 <= n <= 1000
- 0 <= presses <= 1000

