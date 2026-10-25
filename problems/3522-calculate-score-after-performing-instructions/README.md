# 3522. Calculate Score After Performing Instructions
**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Simulation
**Link (online only):** https://leetcode.com/problems/calculate-score-after-performing-instructions/

You are given two arrays, instructions and values, both of size n.
You need to simulate a process based on the following rules:
The process ends when you either:
Return your score at the end of the process.

**Example 1:**
```
Input: instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]
Output: 1
Explanation:
Simulate the process starting at instruction 0:
```

**Example 2:**
```
Input: instructions = ["jump","add","add"], values = [3,1,1]
Output: 0
Explanation:
Simulate the process starting at instruction 0:
```

**Example 3:**
```
Input: instructions = ["jump"], values = [0]
Output: 0
Explanation:
Simulate the process starting at instruction 0:
```

**Constraints:**
- n == instructions.length == values.length
- 1 <= n <= 105
- instructions[i] is either "add" or "jump".
- -105 <= values[i] <= 105

<details><summary>Hints</summary>

1. Simulate the process step by step, following the rules for each instruction.
2. Use a data structure to track which instructions have already been executed to detect revisits.

</details>
