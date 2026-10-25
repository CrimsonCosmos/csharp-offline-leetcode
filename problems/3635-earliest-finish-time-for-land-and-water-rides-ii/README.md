# 3635. Earliest Finish Time for Land and Water Rides II
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

You are given two categories of theme park attractions: land rides and water rides.
A tourist must experience exactly one ride from each category, in either order.
Return the earliest possible time at which the tourist can finish both rides.

**Example 1:**
```
Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
Output: 9
Explanation: ​​​​​​​
Plan A gives the earliest finish time of 9.
```

**Example 2:**
```
Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
Output: 14
Explanation: ​​​​​​​
Plan A provides the earliest finish time of 14. ​​​​​​​
```

**Constraints:**
- 1 <= n, m <= 5 * 104
- landStartTime.length == landDuration.length == n
- waterStartTime.length == waterDuration.length == m
- 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 105

<details><summary>Hints</summary>

1. Sort each ride list by opening time and build a prefix minimum of ride durations and a suffix minimum of ride finish times (<code>start + duration</code>).
2. Try both orders, land then water and water then land. For each ride in the first list compute <code>finish1 = start1 + duration1</code>.
3. Binary‑search the second list (sorted by <code>start</code>) to split rides into those with <code>start <= finish1</code> and those with <code>start > finish1</code>. Use the prefix minimum duration on the early group to get an earliest finish of <code>finish1 + minDuration</code> and the suffix minimum finish time on the late group.
4. For each pairing take the smaller finish time and track the overall minimum.

</details>
