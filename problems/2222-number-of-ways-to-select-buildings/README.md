# 2222. Number of Ways to Select Buildings
**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Prefix Sum
**Link (online only):** https://leetcode.com/problems/number-of-ways-to-select-buildings/

You are given a 0-indexed binary string s which represents the types of buildings along a street where:
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.
Return the number of valid ways to select 3 buildings.

**Example 1:**
```
Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
```

**Example 2:**
```
Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
```

**Constraints:**
- 3 <= s.length <= 105
- s[i] is either '0' or '1'.

<details><summary>Hints</summary>

1. There are only 2 valid patterns: ‘101’ and ‘010’. Think about how we can construct these 2 patterns from smaller patterns.
2. Count the number of subsequences of the form ‘01’ or ‘10’ first. Let n01[i] be the number of ‘01’ subsequences that exist in the prefix of s up to the ith building. How can you compute n01[i]?
3. Let n0[i] and n1[i] be the number of ‘0’s and ‘1’s that exists in the prefix of s up to i respectively. Then n01[i] = n01[i – 1] if s[i] == ‘0’, otherwise n01[i] = n01[i – 1] + n0[i – 1].
4. The same logic applies to building the n10 array and subsequently the n101 and n010 arrays for the number of ‘101’ and ‘010‘ subsequences.

</details>
