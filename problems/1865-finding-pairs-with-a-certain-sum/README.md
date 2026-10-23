# 1865. Finding Pairs With a Certain Sum
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Design
**Link (online only):** https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:
Implement the FindSumPairs class:

**Example 1:**
```
Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
```

**Constraints:**
- 1 <= nums1.length <= 1000
- 1 <= nums2.length <= 105
- 1 <= nums1[i] <= 109
- 1 <= nums2[i] <= 105
- 0 <= index < nums2.length
- 1 <= val <= 105
- 1 <= tot <= 109
- At most 1000 calls are made to add and count each.

<details><summary>Hints</summary>

1. The length of nums1 is small in comparison to that of nums2
2. If we iterate over elements of nums1 we just need to find the count of tot - element for all elements in nums1

</details>
