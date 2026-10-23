# 3097. Shortest Subarray With OR at Least K II
**Difficulty:** Medium  
**Topics:** Array, Bit Manipulation, Sliding Window
**Link (online only):** https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

**Example 1:**
```
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3 . Hence, we return 1 .
```

**Example 2:**
```
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11 . Hence, we return 3 .
```

**Example 3:**
```
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1 . Hence, we return 1 .
```

**Constraints:**
- 1 <= nums.length <= 2 * 105
- 0 <= nums[i] <= 109
- 0 <= k <= 109

<details><summary>Hints</summary>

1. For each <code>nums[i]</code>, we can maintain each subarray’s bitwise <code>OR</code> result ending with it.
2. The property of bitwise <code>OR</code> is that it never unsets any bits and only sets new bits
3. So the number of different results for each <code>nums[i]</code> is at most the number of bits 32.

</details>
