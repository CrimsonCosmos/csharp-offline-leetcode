# 3583. Count Special Triplets
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Counting
**Link (online only):** https://leetcode.com/problems/count-special-triplets/

You are given an integer array nums.
A special triplet is defined as a triplet of indices (i, j, k) such that:
Return the total number of special triplets in the array.
Since the answer may be large, return it modulo 109 + 7.

**Example 1:**
```
Input: nums = [6,3,6]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 1, 2) , where:
```

**Example 2:**
```
Input: nums = [0,1,0,0]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 2, 3) , where:
```

**Example 3:**
```
Input: nums = [8,4,2,8,4]
Output: 2
Explanation:
There are exactly two special triplets:
```

**Constraints:**
- 3 <= n == nums.length <= 105
- 0 <= nums[i] <= 105

<details><summary>Hints</summary>

1. Use frequency arrays or maps, e.g. <code>freqPrev</code> and <code>freqNext</code>—to track how many times each value appears before and after the current index.
2. For each index <code>j</code> in the triplet (<code>i</code>,<code>j</code>,<code>k</code>), compute its contribution to the answer using your freqPrev and freqNext counts.

</details>
