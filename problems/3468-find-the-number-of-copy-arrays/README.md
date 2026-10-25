# 3468. Find the Number of Copy Arrays
**Difficulty:** Medium  
**Topics:** Array, Math
**Link (online only):** https://leetcode.com/problems/find-the-number-of-copy-arrays/

You are given an array original of length n and a 2D array bounds of length n x 2, where bounds[i] = [ui, vi].
You need to find the number of possible arrays copy of length n such that:
Return the number of such arrays.

**Example 1:**
```
Input: original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation:
The possible arrays are:
```

**Example 2:**
```
Input: original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]
Output: 4
Explanation:
The possible arrays are:
```

**Example 3:**
```
Input: original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]
Output: 0
Explanation:
No array is possible.
```

**Constraints:**
- 2 <= n == original.length <= 105
- 1 <= original[i] <= 109
- bounds.length == n
- bounds[i].length == 2
- 1 <= bounds[i][0] <= bounds[i][1] <= 109

<details><summary>Hints</summary>

1. <code>copy[0]</code> uniquely determines all other values.
2. Possible values for <code>copy[0]</code> are in <code>[u[0], v[0]]</code>.
3. From left to right, compute valid ranges for each index by intersecting bounds with the previous range.
4. The answer is the size of the valid range for the last index.

</details>
