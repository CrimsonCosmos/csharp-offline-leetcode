# 2762. Continuous Subarrays
**Difficulty:** Medium  
**Topics:** Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue
**Link (online only):** https://leetcode.com/problems/continuous-subarrays/

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
Return the total number of continuous subarrays.
A subarray is a contiguous non-empty sequence of elements within an array.

**Example 1:**
```
Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.
```

**Example 2:**
```
Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Try using the sliding window technique.
2. Use a set or map to keep track of the maximum and minimum of subarrays.

</details>
