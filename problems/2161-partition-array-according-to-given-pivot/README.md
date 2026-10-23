# 2161. Partition Array According to Given Pivot
**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Simulation
**Link (online only):** https://leetcode.com/problems/partition-array-according-to-given-pivot/

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
Return nums after the rearrangement.

**Example 1:**
```
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
```

**Example 2:**
```
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
```

**Constraints:**
- 1 <= nums.length <= 105
- -106 <= nums[i] <= 106
- pivot equals to an element of nums.

<details><summary>Hints</summary>

1. Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?
2. With the separate lists generated, could you then generate the result?

</details>
