# 777. Swap Adjacent in LR String
**Difficulty:** Medium  
**Topics:** Two Pointers, String
**Link (online only):** https://leetcode.com/problems/swap-adjacent-in-lr-string/

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string result, return True if and only if there exists a sequence of moves to transform start to result.

**Example 1:**
```
Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
Output: true
Explanation: We can transform start to result following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```

**Example 2:**
```
Input: start = "X", result = "L"
Output: false
```

**Constraints:**
- 1 <= start.length <= 104
- start.length == result.length
- Both start and result will only consist of characters in 'L', 'R', and 'X'.

<details><summary>Hints</summary>

1. Think of the L and R's as people on a horizontal line, where X is a space.  The people can't cross each other, and also you can't go from XRX to RXX.

</details>
