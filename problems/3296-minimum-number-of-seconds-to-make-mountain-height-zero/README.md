# 3296. Minimum Number of Seconds to Make Mountain Height Zero
**Difficulty:** Medium  
**Topics:** Array, Math, Binary Search, Greedy, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

You are given an integer mountainHeight denoting the height of a mountain.
You are also given an integer array workerTimes representing the work time of workers in seconds.
The workers work simultaneously to reduce the height of the mountain. For worker i:
Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

**Example 1:**
```
Input: mountainHeight = 4, workerTimes = [2,1,1]
Output: 3
Explanation:
One way the height of the mountain can be reduced to 0 is:
Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.
```

**Example 2:**
```
Input: mountainHeight = 10, workerTimes = [3,2,2,4]
Output: 12
Explanation:
The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.
```

**Example 3:**
```
Input: mountainHeight = 5, workerTimes = [1]
Output: 15
Explanation:
There is only one worker in this example, so the answer is workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15 .
```

**Constraints:**
- 1 <= mountainHeight <= 105
- 1 <= workerTimes.length <= 104
- 1 <= workerTimes[i] <= 106

<details><summary>Hints</summary>

1. Can we use binary search to solve this problem?
2. Do a binary search on the number of seconds to check if it's enough to reduce the mountain height to 0 or less with all workers working simultaneously.

</details>
