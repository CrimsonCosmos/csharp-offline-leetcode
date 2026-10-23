# 3192. Minimum Operations to Make Binary Array Elements Equal to One II
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

You are given a binary array nums.
You can do the following operation on the array any number of times (possibly zero):
Flipping an element means changing its value from 0 to 1, and from 1 to 0.
Return the minimum number of operations required to make all elements in nums equal to 1.

**Example 1:**
```
Input: nums = [0,1,1,0,1]
Output: 4
Explanation: We can do the following operations:
```

**Example 2:**
```
Input: nums = [1,0,0,0]
Output: 1
Explanation: We can do the following operation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 0 <= nums[i] <= 1

<details><summary>Hints</summary>

1. The only way to change <code>nums[0]</code> to 1 is by performing an operation with index <code>i = 0</code>.
2. Iterate from left to right and perform an operation at each index i where nums[i] is 0, and keep track of how many operations are currently performed on the suffix.

</details>
