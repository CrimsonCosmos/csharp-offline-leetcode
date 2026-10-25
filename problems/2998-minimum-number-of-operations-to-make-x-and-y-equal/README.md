# 2998. Minimum Number of Operations to Make X and Y Equal
**Difficulty:** Medium  
**Topics:** Dynamic Programming, Breadth-First Search, Memoization
**Link (online only):** https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

You are given two positive integers x and y.
In one operation, you can do one of the four following operations:
Return the minimum number of operations required to make  x and y equal.

**Example 1:**
```
Input: x = 26, y = 1
Output: 3
Explanation: We can make 26 equal to 1 by applying the following operations: 
1. Decrement x by 1
2. Divide x by 5
3. Divide x by 5
It can be shown that 3 is the minimum number of operations required to make 26 equal to 1.
```

**Example 2:**
```
Input: x = 54, y = 2
Output: 4
Explanation: We can make 54 equal to 2 by applying the following operations: 
1. Increment x by 1
2. Divide x by 11 
3. Divide x by 5
4. Increment x by 1
It can be shown that 4 is the minimum number of operations required to make 54 equal to 2.
```

**Example 3:**
```
Input: x = 25, y = 30
Output: 5
Explanation: We can make 25 equal to 30 by applying the following operations: 
1. Increment x by 1
2. Increment x by 1
3. Increment x by 1
4. Increment x by 1
5. Increment x by 1
It can be shown that 5 is the minimum number of operations required to make 25 equal to 30.
```

**Constraints:**
- 1 <= x, y <= 104

<details><summary>Hints</summary>

1. The only way to make <code>x</code> larger is to increase it by <code>1</code> so if <code>y >= x</code> the answer is <code>y - x</code>.
2. For <code>y < x</code>, <code>x - y</code> is always a candidate answer since we can repeatedly decrease <code>x</code> by one to reach <code>y</code>.
3. We can also increase <code>x</code> and then use the division operations. For example, if <code>x = 10</code> and <code>y = 1</code>, we can increment <code>x</code> by <code>1</code> then divide it by <code>11</code>.
4. Find an upper bound <code>U</code> on the maximum value of <code>x</code> we will reach an optimal solution. Since all values of <code>x</code> will be in the range <code>[1, U]</code>, we can use BFS to find the answer.
5. One possible upper bound on <code>x</code> is <code>U = x + (x - y) </code>. To reach any number strictly greater than <code>U</code> from <code>x</code>, we will need more than <code>x - y</code> operations which is not optimal since we can always reach <code>y</code> in <code>x - y</code> operations.

</details>
