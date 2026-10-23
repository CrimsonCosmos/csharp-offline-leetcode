# 1702. Maximum Binary String After Change
**Difficulty:** Medium  
**Topics:** String, Greedy
**Link (online only):** https://leetcode.com/problems/maximum-binary-string-after-change/

You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

**Example 1:**
```
Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
```

**Example 2:**
```
Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.
```

**Constraints:**
- 1 <= binary.length <= 105
- binary consist of '0' and '1'.

<details><summary>Hints</summary>

1. Note that with the operations, you can always make the string only contain at most 1 zero.

</details>
