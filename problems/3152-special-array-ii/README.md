# 3152. Special Array II
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Prefix Sum
**Link (online only):** https://leetcode.com/problems/special-array-ii/

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.
Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

**Example 1:**
```
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]
Explanation:
The subarray is [3,4,1,2,6] . 2 and 6 are both even.
```

**Example 2:**
```
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105
- 1 <= queries.length <= 105
- queries[i].length == 2
- 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

<details><summary>Hints</summary>

1. Try to split the array into some non-intersected continuous special subarrays.
2. For each query check that the first and the last elements of that query are in the same subarray or not.

</details>
