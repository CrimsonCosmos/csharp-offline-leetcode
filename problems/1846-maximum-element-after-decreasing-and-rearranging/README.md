# 1846. Maximum Element After Decreasing and Rearranging
**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting
**Link (online only):** https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:
There are 2 types of operations that you can perform any number of times:
Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

**Example 1:**
```
Input: arr = [2,2,1,2,1]
Output: 2
Explanation: 
We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
The largest element in arr is 2.
```

**Example 2:**
```
Input: arr = [100,1,1000]
Output: 3
Explanation: 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange arr so it becomes [1,100,1000].
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now arr = [1,2,3], which satisfies the conditions.
The largest element in arr is 3.
```

**Example 3:**
```
Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.
```

**Constraints:**
- 1 <= arr.length <= 105
- 1 <= arr[i] <= 109

<details><summary>Hints</summary>

1. Sort the Array.
2. Decrement each element to the largest integer that satisfies the conditions.

</details>
