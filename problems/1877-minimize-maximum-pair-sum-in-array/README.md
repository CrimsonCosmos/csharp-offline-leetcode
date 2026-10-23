# 1877. Minimize Maximum Pair Sum in Array
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
Return the minimized maximum pair sum after optimally pairing up the elements.

**Example 1:**
```
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
```

**Example 2:**
```
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
```

**Constraints:**
- n == nums.length
- 2 <= n <= 105
- n is even.
- 1 <= nums[i] <= 105

<details><summary>Hints</summary>

1. Would sorting help find the optimal order?
2. Given a specific element, how would you minimize its specific pairwise sum?

</details>
