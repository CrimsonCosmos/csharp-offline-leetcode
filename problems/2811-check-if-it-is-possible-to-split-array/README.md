# 2811. Check if it is Possible to Split Array
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Greedy
**Link (online only):** https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

You are given an array nums of length n and an integer m. You need to determine if it is possible to split the array into n arrays of size 1 by performing a series of steps.
An array is called good if:
In each step, you can select an existing array (which may be the result of previous steps) with a length of at least two and split it into two arrays, if both resulting arrays are good.
Return true if you can split the given array into n arrays, otherwise return false.

**Example 1:**
```
Input: nums = [2, 2, 1], m = 4
Output: true
Explanation:
```

**Example 2:**
```
Input: nums = [2, 1, 3], m = 5
Output: false
Explanation:
The first move has to be either of the following:
So as both moves are invalid (they do not divide the array into two good arrays), we are unable to split nums into n arrays of size 1.
```

**Example 3:**
```
Input: nums = [2, 3, 3, 2, 3], m = 6
Output: true
Explanation:
```

**Constraints:**
- 1 <= n == nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= m <= 200

<details><summary>Hints</summary>

1. It can be proven that if you can split more than one element as a subarray, then you can split exactly one element.

</details>
