# 2241. Design an ATM Machine
**Difficulty:** Medium  
**Topics:** Array, Greedy, Design
**Link (online only):** https://leetcode.com/problems/design-an-atm-machine/

There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.
When withdrawing, the machine prioritizes using banknotes of larger values.
Implement the ATM class:

**Example 1:**
```
Input
["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]
Output
[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]

Explanation
ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // Deposits 1 $100 banknote, 2 $200 banknotes,
                          // and 1 $500 banknote.
atm.withdraw(600);        // Returns [0,0,1,0,1]. The machine uses 1 $100 banknote
                          // and 1 $500 banknote. The banknotes left over in the
                          // machine are [0,0,0,2,0].
atm.deposit([0,1,0,1,1]); // Deposits 1 $50, $200, and $500 banknote.
                          // The banknotes in the machine are now [0,1,0,3,1].
atm.withdraw(600);        // Returns [-1]. The machine will try to use a $500 banknote
                          // and then be unable to complete the remaining $100,
                          // so the withdraw request will be rejected.
                          // Since the request is rejected, the number of banknotes
                          // in the machine is not modified.
atm.withdraw(550);        // Returns [0,1,0,0,1]. The machine uses 1 $50 banknote
                          // and 1 $500 banknote.
```

**Constraints:**
- banknotesCount.length == 5
- 0 <= banknotesCount[i] <= 109
- 1 <= amount <= 109
- At most 5000 calls in total will be made to withdraw and deposit.
- At least one call will be made to each function withdraw and deposit.
- Sum of banknotesCount[i] in all deposits doesn't exceed 109

<details><summary>Hints</summary>

1. Store the number of banknotes of each denomination.
2. Can you use math to quickly evaluate a withdrawal request?

</details>
