# 3424. Minimum Cost to Make Arrays Identical
**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

You are given two integer arrays arr and brr of length n, and an integer k. You can perform the following operations on arr any number of times:
Return the minimum total cost to make arr equal to brr.

**Example 1:**
```
Input: arr = [-7,9,5], brr = [7,-2,-5], k = 2
Output: 13
Explanation:
The total cost to make the arrays equal is 2 + 2 + 7 + 2 = 13 .
```

**Example 2:**
```
Input: arr = [2,1], brr = [2,1], k = 0
Output: 0
Explanation:
Since the arrays are already equal, no operations are needed, and the total cost is 0.
```

**Constraints:**
- 1 <= arr.length == brr.length <= 105
- 0 <= k <= 2 * 1010
- -105 <= arr[i] <= 105
- -105 <= brr[i] <= 105

<details><summary>Hints</summary>

1. What does Operation 1 (rearranging subarrays) actually accomplish?
2. Calculate <code>sum(abs(arr[i] - brr[i]))</code> if you do not use Operation 1.
3. Calculate <code>sum(abs(arr[i] - brr[i]))</code> after sorting both arrays if you use Operation 1.

</details>
