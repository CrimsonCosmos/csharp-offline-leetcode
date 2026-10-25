# 3638. Maximum Balanced Shipments
**Difficulty:** Medium  
**Topics:** 
**Link (online only):** https://leetcode.com/problems/maximum-balanced-shipments/

You are given an integer array weight of length n, representing the weights of n parcels arranged in a straight line. A shipment is defined as a contiguous subarray of parcels. A shipment is considered balanced if the weight of the last parcel is strictly less than the maximum weight among all parcels in that shipment.
Select a set of non-overlapping, contiguous, balanced shipments such that each parcel appears in at most one shipment (parcels may remain unshipped).
Return the maximum possible number of balanced shipments that can be formed.

**Example 1:**
```
Input: weight = [2,5,1,4,3]
Output: 2
Explanation:
We can form the maximum of two balanced shipments as follows:
It is impossible to partition the parcels to achieve more than two balanced shipments, so the answer is 2.
```

**Example 2:**
```
Input: weight = [4,4]
Output: 0
Explanation:
No balanced shipment can be formed in this case:
As there is no way to form even one balanced shipment, the answer is 0.
```

**Constraints:**
- 2 <= n <= 105
- 1 <= weight[i] <= 109

<details><summary>Hints</summary>

1. Use a monotonic stack to find for each end index <code>i</code> the nearest previous index <code>j</code> with <code>weight[j] > weight[i]</code> (set <code>j = -1</code> if none).
2. Then set <code>dp[i] = best[j] + 1</code> (using <code>best[-1] = 0</code>), and update <code>best[i] = max(best[i-1], dp[i])</code>; the result is <code>best[n-1]</code>.

</details>
