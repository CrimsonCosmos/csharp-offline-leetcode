# 3259. Maximum Energy Boost From Two Drinks
**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming
**Link (online only):** https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

You are given two integer arrays energyDrinkA and energyDrinkB of the same length n by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.
You want to maximize your total energy boost by drinking one energy drink per hour. However, if you want to switch from consuming one energy drink to the other, you need to wait for one hour to cleanse your system (meaning you won't get any energy boost in that hour).
Return the maximum total energy boost you can gain in the next n hours.
Note that you can start consuming either of the two energy drinks.

**Example 1:**
```
Input: energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]
Output: 5
Explanation:
To gain an energy boost of 5, drink only the energy drink A (or only B).
```

**Example 2:**
```
Input: energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]
Output: 7
Explanation:
To gain an energy boost of 7:
```

**Constraints:**
- n == energyDrinkA.length == energyDrinkB.length
- 3 <= n <= 105
- 1 <= energyDrinkA[i], energyDrinkB[i] <= 105

<details><summary>Hints</summary>

1. Can we solve it using dynamic programming?
2. Define <code>dpA[i]</code> as the maximum energy boost if we consider only the first <code>i + 1</code> hours such that in the last hour, we drink the energy drink A.
3. Similarly define <code>dpB[i]</code>.
4. <code>dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]</code>
5. Similarly, fill <code>dpB</code>.
6. The answer is <code>max(dpA[n - 1], dpB[n - 1])</code>.

</details>
