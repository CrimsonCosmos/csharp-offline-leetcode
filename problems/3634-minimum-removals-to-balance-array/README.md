# 3634. Minimum Removals to Balance Array
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/minimum-removals-to-balance-array/

You are given an integer array nums and an integer k.
An array is considered balanced if the value of its maximum element is at most k times the minimum element.
You may remove any number of elements from nums​​​​​​​ without making it empty.
Return the minimum number of elements to remove so that the remaining array is balanced.
Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

**Example 1:**
```
Input: nums = [2,1,5], k = 2
Output: 1
Explanation:
```

**Example 2:**
```
Input: nums = [1,6,2,9], k = 3
Output: 2
Explanation:
```

**Example 3:**
```
Input: nums = [4,6], k = 2
Output: 0
Explanation:
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- 1 <= k <= 105

<details><summary>Hints</summary>

1. Sort <code>nums</code> and use two pointers <code>i</code> and <code>j</code> so that the window's minimum is <code>nums[i]</code> and maximum is <code>nums[j]</code>.
2. Expand <code>j</code> while <code>nums[j] <= k * nums[i]</code> to maximize the balanced window; answer = <code>n - (j - i + 1)</code>.

</details>
