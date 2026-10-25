# 3020. Find the Maximum Number of Elements in Subset
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Enumeration
**Link (online only):** https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

You are given an array of positive integers nums.
You need to select a subset of nums which satisfies the following condition:
Return the maximum number of elements in a subset that satisfies these conditions.

**Example 1:**
```
Input: nums = [5,4,1,2,2]
Output: 3
Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.
```

**Example 2:**
```
Input: nums = [1,3,2,4]
Output: 1
Explanation: We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer.
```

**Constraints:**
- 2 <= nums.length <= 105
- 1 <= nums[i] <= 109

<details><summary>Hints</summary>

1. We can select an odd number of <code>1</code>’s.
2. Put all the values into a HashSet. We can start from each <code>x > 1</code> as the smallest chosen value and we can find the longest subset by checking the new values (which are the square of the previous value) in the set by brute force.
3. Note when <code>x > 1</code>, <code>x<sup>2</sup></code>, <code>x<sup>4</sup></code>, <code>x<sup>8</sup></code>, … increases very fast, the longest subset with smallest value x cannot be very long. (The length is <code>O(log(log(10<sup>9</sup>)))</code>.
4. Hence we can directly check all lengths less than <code>10</code> for all values of <code>x</code>.

</details>
