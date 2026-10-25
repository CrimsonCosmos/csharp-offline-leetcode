# 3478. Choose K Elements With Maximum Sum
**Difficulty:** Medium  
**Topics:** Array, Sorting, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.
For each index i from 0 to n - 1, perform the following:
Return an array answer of size n, where answer[i] represents the result for the corresponding index i.

**Example 1:**
```
Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2
Output: [80,30,0,80,50]
Explanation:
```

**Example 2:**
```
Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1
Output: [0,0,0,0]
Explanation:
Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i , resulting in 0 for all positions.
```

**Constraints:**
- n == nums1.length == nums2.length
- 1 <= n <= 105
- 1 <= nums1[i], nums2[i] <= 106
- 1 <= k <= n

<details><summary>Hints</summary>

1. Sort <code>nums1</code> and its corresponding <code>nums2</code> values together based on <code>nums1</code>.
2. Use a max heap to track the top <code>k</code> values of <code>nums2</code> as you process each element in the sorted order.

</details>
