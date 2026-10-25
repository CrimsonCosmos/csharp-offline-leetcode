# 3159. Find Occurrences of an Element in an Array
**Difficulty:** Medium  
**Topics:** Array, Hash Table
**Link (online only):** https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

You are given an integer array nums, an integer array queries, and an integer x.
For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
Return an integer array answer containing the answers to all queries.

**Example 1:**
```
Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1
Output: [0,-1,2,-1]
Explanation:
```

**Example 2:**
```
Input: nums = [1,2,3], queries = [10], x = 5
Output: [-1]
Explanation:
```

**Constraints:**
- 1 <= nums.length, queries.length <= 105
- 1 <= queries[i] <= 105
- 1 <= nums[i], x <= 104

<details><summary>Hints</summary>

1. Compress the array <code>nums</code> and save all the occurrences of each element in the separate arrays.

</details>
