# 3551. Minimum Swaps to Sort by Digit Sum
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Sorting
**Link (online only):** https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.
Return the minimum number of swaps required to rearrange nums into this sorted order.
A swap is defined as exchanging the values at two distinct positions in the array.

**Example 1:**
```
Input: nums = [37,100]
Output: 1
Explanation:
```

**Example 2:**
```
Input: nums = [22,14,33,7]
Output: 0
Explanation:
```

**Example 3:**
```
Input: nums = [18,43,34,16]
Output: 2
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- nums consists of distinct positive integers.

<details><summary>Hints</summary>

1. First, sort the array based on digit sum (and value as a tiebreaker). Then, map each original value to its index in the sorted array.
2. Now, the problem reduces to finding the minimum number of swaps to sort this mapped array. The answer is <code>n - number_of_cycles</code> in the permutation.

</details>
