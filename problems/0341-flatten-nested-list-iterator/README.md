# 341. Flatten Nested List Iterator
**Difficulty:** Medium  
**Topics:** Stack, Tree, Depth-First Search, Design, Queue, Iterator
**Link (online only):** https://leetcode.com/problems/flatten-nested-list-iterator/

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.
Implement the NestedIterator class:
Your code will be tested with the following pseudocode:
If res matches the expected flattened list, then your code will be judged as correct.

**Example 1:**
```
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```

**Example 2:**
```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```

**Example 3:**
```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```

**Constraints:**
- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-106, 106].

