# 3629. Minimum Jumps to Reach End via Prime Teleportation
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

You are given an integer array nums of length n.
You start at index 0, and your goal is to reach index n - 1.
From any index i, you may perform one of the following operations:
Return the minimum number of jumps required to reach index n - 1.

**Example 1:**
```
Input: nums = [1,2,4,6]
Output: 2
Explanation:
One optimal sequence of jumps is:
Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,3,4,7,9]
Output: 2
Explanation:
One optimal sequence of jumps is:
Thus, the answer is 2.
```

**Example 3:**
```
Input: nums = [4,6,5,8]
Output: 3
Explanation:
```

**Constraints:**
- 1 <= n == nums.length <= 105
- 1 <= nums[i] <= 106

<details><summary>Hints</summary>

1. Use a breadth-first search.
2. Precompute prime factors of each <code>nums[i]</code> via a sieve, and build a bucket <code>bucket[p]</code> mapping each prime <code>p</code> to all indices <code>j</code> with <code>nums[j] % p == 0</code>.
3. During the BFS, when at index <code>i</code>, enqueue its adjacent steps (<code>i+1</code> and <code>i-1</code>) and all indices in <code>bucket[p]</code> for each prime <code>p</code> dividing <code>nums[i]</code>, then clear <code>bucket[p]</code> so each prime's bucket is visited only once.

</details>
