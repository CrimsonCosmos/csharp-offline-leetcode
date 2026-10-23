# 2910. Minimum Number of Groups to Create a Valid Assignment
**Difficulty:** Medium  
**Topics:** Array, Hash Table, Greedy
**Link (online only):** https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

You are given a collection of numbered balls and instructed to sort them into boxes for a nearly balanced distribution. There are two rules you must follow:
​Return the fewest number of boxes to sort these balls following these rules.

**Example 1:**
```
Input: balls = [3,2,3,2,3]
Output: 2
Explanation:
We can sort balls into boxes as follows:
The size difference between the two boxes doesn't exceed one.
```

**Example 2:**
```
Input: balls = [10,10,10,3,1,1]
Output: 4
Explanation:
We can sort balls into boxes as follows:
You can't use fewer than four boxes while still following the rules. For example, putting all three balls numbered 10 in one box would break the rule about the maximum size difference between boxes.
```

**Constraints:**
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109

<details><summary>Hints</summary>

1. Calculate the frequency of each number.
2. For each <code>x</code> in the range <code>[1, minimum_frequency]</code>, try to create groups with either <code>x</code> or <code>x + 1</code> indices assigned to them while minimizing the total number of groups.
3. For each distinct number, using its frequency, check that all its occurrences can be assigned to groups of size <code>x</code> or <code>x + 1</code> while minimizing the number of groups used.
4. To get the minimum number of groups needed for a number having frequency <code>f</code> to be assigned to groups of size <code>x</code> or <code>x + 1</code>, let <code>a = f / (x + 1)</code> and <code>b = f % (x + 1)</code>. <ul> <li>If <code>b == 0</code>, then we can simply create <code>a</code> groups of size <code>x + 1</code>.</li> <li>If <code>x - b <= a</code>, we can have <code>a - (x - b)</code> groups of size <code>x + 1</code> and <code>x - b + 1</code> groups of size <code>x</code>. So, in total, we have <code>a + 1</code> groups.</li> <li>Otherwise, it's impossible.</li> </ul>
5. The minimum number of groups needed for some <code>x</code> is the total minimized number of groups needed for each distinct number.
6. The answer is the minimum number of groups needed for each <code>x</code> in the range <code>[1, minimum_frequency]</code>.

</details>
