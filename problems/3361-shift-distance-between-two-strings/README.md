# 3361. Shift Distance Between Two Strings
**Difficulty:** Medium  
**Topics:** Array, String, Prefix Sum
**Link (online only):** https://leetcode.com/problems/shift-distance-between-two-strings/

You are given two strings s and t of the same length, and two integer arrays nextCost and previousCost.
In one operation, you can pick any index i of s, and perform either one of the following actions:
The shift distance is the minimum total cost of operations required to transform s into t.
Return the shift distance from s to t.

**Example 1:**
```
Input: s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: 2
Explanation:
```

**Example 2:**
```
Input: s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Output: 31
Explanation:
```

**Constraints:**
- 1 <= s.length == t.length <= 105
- s and t consist only of lowercase English letters.
- nextCost.length == previousCost.length == 26
- 0 <= nextCost[i], previousCost[i] <= 109

<details><summary>Hints</summary>

1. - For every unordered pair of characters <code>(a, b)</code>, the cost of turning <code>a</code> into <code>b</code> is equal to the minimum between: 
<ul>
<li>If <code>i < j</code>, <code>nextCost[i] + nextCost[i + 1] + … + nextCost[j - 1]</code>, and <code>nextCost[i] + nextCost[i + 1] + … + nextCost[25] + nextCost[0] + … + nextCost[j - 1]</code> otherwise.</li>
    
    <li>If <code>i < j</code>, <code>prevCost[i] + prevCost[i - 1] + … + prevCost[0] + prevCost[25] + … + prevCost[j + 1]</code>, and <code>prevCost[i] + prevCost[i - 1] + … + prevCost[j + 1]</code> otherwise.</li>
    </ul>
    Where <code>i</code> and <code>j</code> are the indices of <code>a</code> and <code>b</code> in the alphabet.
2. The shift distance is the sum of costs of turning <code>s[i]</code> into <code>t[i]</code>.

</details>
