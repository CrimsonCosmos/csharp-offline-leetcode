# 3589. Count Prime-Gap Balanced Subarrays
**Difficulty:** Medium  
**Topics:** Array, Math, Queue, Sliding Window, Number Theory, Monotonic Queue
**Link (online only):** https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

You are given an integer array nums and an integer k.
A subarray is called prime-gap balanced if:
Return the count of prime-gap balanced subarrays in nums.
Note:

**Example 1:**
```
Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
Prime-gap balanced subarrays are:
Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,3,5,7], k = 3
Output: 4
Explanation:
Prime-gap balanced subarrays are:
Thus, the answer is 4.
```

**Constraints:**
- 1 <= nums.length <= 5 * 104
- 1 <= nums[i] <= 5 * 104
- 0 <= k <= 5 * 104

<details><summary>Hints</summary>

1. Sieve and extract primes.
2. Build a sparse-table for <code>O(1)</code> max–min queries.
3. For each prime, binary‐search the furthest valid partner.
4. Count subarrays via left/right gap multiplication.

</details>
