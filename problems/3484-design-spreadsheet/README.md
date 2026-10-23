# 3484. Design Spreadsheet
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Design, Matrix
**Link (online only):** https://leetcode.com/problems/design-spreadsheet/

A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.
Implement the Spreadsheet class:
Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

**Example 1:**
```
Input: ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"] [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
Output: [null, 12, null, 16, null, 25, null, 15]
Explanation
```

**Constraints:**
- 1 <= rows <= 103
- 0 <= value <= 105
- The formula is always in the format "=X+Y", where X and Y are either valid cell references or non-negative integers with values less than or equal to 105.
- Each cell reference consists of a capital letter from 'A' to 'Z' followed by a row number between 1 and rows.
- At most 104 calls will be made in total to setCell, resetCell, and getValue.

<details><summary>Hints</summary>

1. Use a hashmap to represent the cells, where the key is the cell reference (e.g., <code>"A1"</code>) and the value is the integer stored in the cell.
2. For <code>setCell</code>, simply assign the given value to the specified cell in the hashmap.
3. For <code>resetCell</code>, set the value of the specified cell to <code>0</code> in the hashmap.
4. For <code>getValue</code>, find the values of the operands from the hashmap and return their sum.

</details>
