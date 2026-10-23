# 1488. Avoid Flood in The City
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Binary Search, Greedy, Heap (Priority Queue)
**Link (online only):** https://leetcode.com/problems/avoid-flood-in-the-city/

Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.
Given an integer array rains where:
Return an array ans where:
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

**Example 1:**
```
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
```

**Example 2:**
```
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
```

**Example 3:**
```
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
```

**Constraints:**
- 1 <= rains.length <= 105
- 0 <= rains[i] <= 109

<details><summary>Hints</summary>

1. Keep An array of the last day there was rains over each city.
2. Keep an array of the days you can dry a lake when you face one.
3. When it rains over a lake, check the first possible day you can dry this lake and assign this day to this lake.

</details>
