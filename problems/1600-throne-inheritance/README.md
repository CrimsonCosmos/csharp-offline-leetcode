# 1600. Throne Inheritance
**Difficulty:** Medium  
**Topics:** Hash Table, Tree, Depth-First Search, Design
**Link (online only):** https://leetcode.com/problems/throne-inheritance/

A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.
The kingdom has a well-defined order of inheritance that consists of the king as the first member. Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.
For example, assume we have a kingdom that consists of the king, his children Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.
Using the above function, we can always obtain a unique order of inheritance.
Implement the ThroneInheritance class:

**Example 1:**
```
Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
```

**Example 2:**
```
Input
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
Output
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

Explanation
ThroneInheritance t= new ThroneInheritance("king"); // order: king
t.birth("king", "andy"); // order: king > andy
t.birth("king", "bob"); // order: king > andy > bob
t.birth("king", "catherine"); // order: king > andy > bob > catherine
t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]
```

**Constraints:**
- 1 <= kingName.length, parentName.length, childName.length, name.length <= 15
- kingName, parentName, childName, and name consist of lowercase English letters only.
- All arguments childName and kingName are distinct.
- All name arguments of death will be passed to either the constructor or as childName to birth first.
- For each call to birth(parentName, childName), it is guaranteed that parentName is alive.
- At most 105 calls will be made to birth and death.
- At most 10 calls will be made to getInheritanceOrder.

<details><summary>Hints</summary>

1. Create a tree structure of the family.
2. Without deaths, the order of inheritance is simply a pre-order traversal of the tree.
3. Mark the dead family members tree nodes and don't include them in the final order.

</details>
