# 3494. Find the Minimum Amount of Time to Brew Potions
**Difficulty:** Medium  
**Topics:** Array, Simulation, Prefix Sum
**Link (online only):** https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

You are given two integer arrays, skill and mana, of length n and m, respectively.
In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].
Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​
Return the minimum amount of time required for the potions to be brewed properly.

**Example 1:**
```
Input: skill = [1,5,2,4], mana = [5,1,4,2]
Output: 110
Explanation:
As an example for why wizard 0 cannot start working on the 1 st potion before time t = 52 , consider the case where the wizards started preparing the 1 st potion at time t = 50 . At time t = 58 , wizard 2 is done with the 1 st potion, but wizard 3 will still be working on the 0 th potion till time t = 60 .
```

**Example 2:**
```
Input: skill = [1,1,1], mana = [1,1,1]
Output: 5
Explanation:
```

**Example 3:**
```
Input: skill = [1,2,3,4], mana = [1,2]
Output: 21
```

**Constraints:**
- n == skill.length
- m == mana.length
- 1 <= n, m <= 5000
- 1 <= mana[i], skill[i] <= 5000

<details><summary>Hints</summary>

1. Maintain each wizard's earliest free time (for the last potion) as <code>f[i]</code>.
2. Let <code>x</code> be the current mana value. Starting from <code>now = f[0]</code>, update <code>now = max(now + skill[i - 1] * x, f[i])</code> for <code>i in [1..n]</code>. Then, the final <code>f[n - 1] = now + skill[n - 1] * x</code> for this potion.
3. Update all other <code>f</code> values by <code>f[i] = f[i + 1] - skill[i + 1] * x</code> for <code>i in [0..n - 2]</code> (in reverse order).

</details>
