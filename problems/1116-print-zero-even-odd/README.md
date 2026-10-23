# 1116. Print Zero Even Odd
**Difficulty:** Medium  
**Topics:** Concurrency
**Link (online only):** https://leetcode.com/problems/print-zero-even-odd/

You have a function printNumber that can be called with an integer parameter and prints it to the console.
You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:
Modify the given class to output the series "010203040506..." where the length of the series must be 2n.
Implement the ZeroEvenOdd class:

**Example 1:**
```
Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.
```

**Example 2:**
```
Input: n = 5
Output: "0102030405"
```

**Constraints:**
- 1 <= n <= 1000

