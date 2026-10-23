# 12. Integer to Roman
**Difficulty:** Medium  
**Topics:** Hash Table, Math, String
**Link (online only):** https://leetcode.com/problems/integer-to-roman/

Seven different symbols represent Roman numerals with the following values:
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
Given an integer, convert it to a Roman numeral.

**Example 1:**
```
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
```

**Example 2:**
```
50 = L
 8 = VIII
```

**Example 3:**
```
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

**Constraints:**
- 1 <= num <= 3999

