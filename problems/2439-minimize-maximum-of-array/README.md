# 2439. Minimize Maximum of Array
**Difficulty:** Medium  
**Topics:** Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum
**Link (online only):** https://leetcode.com/problems/minimize-maximum-of-array/

You are given a 0-indexed array nums comprising of n non-negative integers.
In one operation, you must:
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

**Example 1:**
```
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
```

**Example 2:**
```
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
```

**Constraints:**
- n == nums.length
- 2 <= n <= 105
- 0 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Try a binary search approach.
2. Perform a binary search over the minimum value that can be achieved for the maximum number of the array.
3. In each binary search iteration, iterate through the array backwards, greedily decreasing the current element until it is within the limit.

</details>
