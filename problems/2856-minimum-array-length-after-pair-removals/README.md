# 2856. Minimum Array Length After Pair Removals
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Two Pointers, Binary Search, Greedy, Counting
**Link (online only):** https://leetcode.com/problems/minimum-array-length-after-pair-removals/

Given an integer array num sorted in non-decreasing order.
You can perform the following operation any number of times:
Return the minimum length of nums after applying the operation zero or more times.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: 0
Explanation:
```

**Example 2:**
```
Input: nums = [1,1,2,2,3,3]
Output: 0
Explanation:
```

**Example 3:**
```
Input: nums = [1000000000,1000000000]
Output: 2
Explanation:
Since both numbers are equal, they cannot be removed.
```

**Example 4:**
```
Input: nums = [2,3,4,4,4]
Output: 1
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- nums is sorted in non-decreasing order.

<details><summary>Hints</summary>

1. To minimize the length of the array, we should maximize the number of operations performed.
2. To perform <code>k</code> operations, it is optimal to use the smallest <code>k</code> values and the largest <code>k</code> values in <code>nums</code>.
3. What is the best way to make pairs from the smallest <code>k</code> values and the largest <code>k</code> values so it is possible to remove all the pairs?
4. If we consider the smallest <code>k</code> values and the largest <code>k</code> values as two separate <strong>sorted 0-indexed</strong> arrays, <code>a</code> and <code>b</code>, It is optimal to pair <code>a[i]</code> and <code>b[i]</code>. So, a <code>k</code> is valid if <code>a[i] < b[i]</code> for all <code>i</code> in the range <code>[0, k - 1]</code>.
5. The greatest possible valid <code>k</code> can be found using binary search.
6. The answer is <code>nums.length - 2 * k</code>.

</details>
