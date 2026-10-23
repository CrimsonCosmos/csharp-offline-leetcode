# 3627. Maximum Median Sum of Subsequences of Size 3
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

You are given an integer array nums with a length divisible by 3.
You want to make the array empty in steps. In each step, you can select any three elements from the array, compute their median, and remove the selected elements from the array.
The median of an odd-length sequence is defined as the middle element of the sequence when it is sorted in non-decreasing order.
Return the maximum possible sum of the medians computed from the selected elements.

**Example 1:**
```
Input: nums = [2,1,3,2,1,3]
Output: 5
Explanation:
Hence, the sum of the medians is 3 + 2 = 5 .
```

**Example 2:**
```
Input: nums = [1,1,10,10,10,10]
Output: 20
Explanation:
Hence, the sum of the medians is 10 + 10 = 20 .
```

**Constraints:**
- 1 <= nums.length <= 5 * 105
- nums.length % 3 == 0
- 1 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Sort the values in <code>nums</code>.
2. Repeatedly pick the largest 2 values and the minimum value.

</details>
