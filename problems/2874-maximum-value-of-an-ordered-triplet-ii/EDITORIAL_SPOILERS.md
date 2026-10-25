[TOC]

## Solution

--- 

### Approach 1: Greedy + Prefix Suffix Array

#### Intuition

Let the length of the array $\textit{nums}$ be $n$. According to the value formula $(\textit{nums}[i] - \textit{nums}[j]) \times \textit{nums}[k]$, it can be known that when $j$ is fixed, the maximum value of the triplet is achieved when $\textit{nums}[i]$ and $\textit{nums}[k]$ respectively take the maximum values from $[0, j)$ and $[j + 1, n)$. We use $\textit{leftMax}[j]$ and $\textit{rightMax}[j]$ to maintain the maximum value of the prefix $[0, j)$ and the maximum value of the suffix $[j + 1, n)$, respectively, and enumerate $j$ in order, calculate the value $(\textit{leftMax}[j] - \textit{nums}[j]) \times \textit{rightMax}[j]$, and return the maximum value (if all values are negative, return $0$).

#### Implementation#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

During the traversal of the array, the prefix and suffix arrays can be maintained, thus achieving a single traversal.

- Space complexity: $O(n)$.

Two arrays are needed to maintain the maximum and minimum values of the prefixes and suffixes.

### Approach 2: Greedy

#### Intuition

Similar to approach 1, if we fix $k$, then the value of the triplet is maximized when $\textit{nums}[i] - \textit{nums}[j]$ takes the maximum value. We can use $\textit{imax}$ to maintain the maximum value of $\textit{nums}[i]$, and $\textit{dmax}$ to maintain the maximum value of $\textit{nums}[i] - \textit{nums}[j]$. During the enumeration of $k$, update $\textit{dmax}$ and $\textit{imax}$.

#### Implementation#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

Similar to approach 1, in the process of a single traversal, the maximum and minimum values can be maintained.

- Space complexity: $O(1)$.

We only need two variables to maintain the maximum and minimum values.

---
