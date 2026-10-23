# 3224. Minimum Array Changes to Make Differences Equal
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum
**Link (online only):** https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

You are given an integer array nums of size n where n is even, and an integer k.
You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from 0 to k.
You need to perform some changes (possibly none) such that the final array satisfies the following condition:
Return the minimum number of changes required to satisfy the above condition.

**Example 1:**
```
Input: nums = [1,0,1,2,4,3], k = 4
Output: 2
Explanation: We can perform the following changes:
The integer X will be 2.
```

**Example 2:**
```
Input: nums = [0,1,2,3,3,6,5,4], k = 6
Output: 2
Explanation: We can perform the following operations:
The integer X will be 4.
```

**Constraints:**
- 2 <= n == nums.length <= 105
- n is even.
- 0 <= nums[i] <= k <= 105

<details><summary>Hints</summary>

1. There are at most <code>k + 1</code> possible values of the integer <code>X</code>.
2. How do we calculate the minimum number of changes efficiently if we fix the value of <code>X</code> before applying any changes?

</details>
