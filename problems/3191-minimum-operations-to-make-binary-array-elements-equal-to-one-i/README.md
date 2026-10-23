# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
**Difficulty:** Medium  
**Topics:** Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum
**Link (online only):** https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

You are given a binary array nums.
You can do the following operation on the array any number of times (possibly zero):
Flipping an element means changing its value from 0 to 1, and from 1 to 0.
Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

**Example 1:**
```
Input: nums = [0,1,1,1,0,0]
Output: 3
Explanation: We can do the following operations:
```

**Example 2:**
```
Input: nums = [0,1,1,1]
Output: -1
Explanation: It is impossible to make all elements equal to 1.
```

**Constraints:**
- 3 <= nums.length <= 105
- 0 <= nums[i] <= 1

<details><summary>Hints</summary>

1. If <code>nums[0]</code> is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.
2. After Changing <code>nums[0]</code> to 1, use the same logic on the remaining array.

</details>
