# 2593. Find Score of an Array After Marking All Elements
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation
**Link (online only):** https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

You are given an array nums consisting of positive integers.
Starting with score = 0, apply the following algorithm:
Return the score you get after applying the above algorithm.

**Example 1:**
```
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
```

**Example 2:**
```
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 106

<details><summary>Hints</summary>

1. Try simulating the process of marking the elements and their adjacent.
2. If there is an element that was already marked, then you skip it.

</details>
