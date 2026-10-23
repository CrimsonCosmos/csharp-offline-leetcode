# 1146. Snapshot Array
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Binary Search, Design
**Link (online only):** https://leetcode.com/problems/snapshot-array/

Implement a SnapshotArray that supports the following interface:

**Example 1:**
```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

**Constraints:**
- 1 <= length <= 5 * 104
- 0 <= index < length
- 0 <= val <= 109
- 0 <= snap_id < (the total number of times we call snap())
- At most 5 * 104 calls will be made to set, snap, and get.

<details><summary>Hints</summary>

1. Use a list of lists, adding both the element and the snap_id to each index.

</details>
