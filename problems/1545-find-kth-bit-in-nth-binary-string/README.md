# 1545. Find Kth Bit in Nth Binary String
**Difficulty:** Medium  
**Topics:** String, Recursion, Simulation
**Link (online only):** https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

Given two positive integers n and k, the binary string Sn is formed as follows:
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

**Example 1:**
```
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
```

**Example 2:**
```
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
```

**Constraints:**
- 1 <= n <= 20
- 1 <= k <= 2n - 1

<details><summary>Hints</summary>

1. Since n is small, we can simply simulate the process of constructing S1 to Sn.

</details>
