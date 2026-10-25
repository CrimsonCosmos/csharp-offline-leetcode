### Approach 1: Square Root Decomposition

#### Intuition

This problem is similar to [3479. Fruits Into Baskets II](https://leetcode.com/problems/fruits-into-baskets-ii/description/), but the difference lies in the **larger input size**, making a direct simulation inefficient.

To optimize, we apply a **square root decomposition** approach.

We divide the `baskets` array into $\sqrt{n}$ blocks, each of size $m = \sqrt{n}$ (approximately). For each block, we maintain the **maximum value** in that block in an auxiliary array `maxV`.

For each fruit, we scan these blocks **block by block**. There are two possibilities for a given block:

1. If the maximum basket capacity in the current block is **less than** the fruit’s quantity, we **skip** this block entirely.
2. If the block contains a basket that can hold the fruit (`maxV[sec] >= fruit`), we scan that block to find the **leftmost** basket that can hold the fruit, place it (set it to 0), and update the block’s maximum value.

If no such basket is found after scanning all blocks, we increment the count of **unplaced fruits**.

#### Implementation#### Complexity Analysis

Let $n$ be the length of the array $\textit{baskets}$.

- Time complexity: $O(n \times \sqrt{n}) = O(n^{\frac32})$.
  
  Enumerating the fruits in $\textit{fruits}$ requires $O(n)$ time, and traversing each block takes $O(\sqrt{n})$ time.

- Space complexity: $O(\sqrt{n})$.
  
  We need to maintain the maximum capacity of the baskets in each block.

---

### Approach 2: Segment Tree + Binary Search

#### Intuition

This is a template problem for a segment tree, where we can use a segment tree to maintain the maximum value of the $\textit{baskets}$ array over intervals, and then use binary search to find the first basket that meets the condition. The specific method is as follows:

1. First, establish a tree where the content maintained at initialization is the maximum value of each interval.
2. Then, enumerate the fruits in $\textit{fruits}$, and use the segment tree to find the maximum value in the interval during the binary search process to locate the first basket that meets the condition. If such a basket is found, use the segment tree to perform a single-point update on that basket, setting its value to $0$. Otherwise, increment the counter $\textit{count}$.
3. The process of binary search is as follows: If the maximum value in the left interval is greater than the current number of fruits, continue the binary search in the left interval. If the maximum value in the left interval is less than the current number of fruits and the maximum value in the right interval is greater than or equal to the current number of fruits, continue the binary search in the right interval. Otherwise, there is no interval that meets the condition in the current range.

#### Implementation#### Complexity Analysis

Let $n$ be the length of the array $\textit{baskets}$.

- Time complexity: $O(n \log n)$.
  
  Constructing the segment tree takes $O(n)$ time. Enumerating the fruits in $\textit{fruits}$ requires $O(n)$ time, and each binary search, segment tree query, and update operation takes $O(\log n)$ time.

- Space complexity: $O(n)$.
  
  It requires $O(n)$ space to store the segment tree.
  
---
