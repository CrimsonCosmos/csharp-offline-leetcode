# 3164. Find the Number of Good Pairs II
**Difficulty:** Medium  
**Topics:** Array, Hash Table
**Link (online only):** https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Return the total number of good pairs.

**Example 1:**
```
Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1
Output: 5
Explanation:
```

**Example 2:**
```
Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3
Output: 2
Explanation:
The 2 good pairs are (3, 0) and (3, 1) .
```

**Constraints:**
- 1 <= n, m <= 105
- 1 <= nums1[i], nums2[j] <= 106
- 1 <= k <= 103

<details><summary>Hints</summary>

1. Let <code>f[v]</code> be the number of occurrences of <code>v/k</code> in nums2.
2. For each value <code>v</code> in nums1, enumerating all its factors <code>d</code> (in <code>sqrt(v)</code> time) and sum up all the <code>f[d]</code> to get the final answer.
3. It is also possible to improve the complexity from <code>len(nums1) * sqrt(v)</code> to <code>len(nums1) * log(v)</code> - How?

</details>
