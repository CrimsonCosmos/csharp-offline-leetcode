[TOC]

## Solution

---

### Approach 1: Sieve of Eratosthenes

#### Intuition

We are given two numbers, `left` and `right`, and we need to find a pair of prime numbers within this range such that their difference is minimized. If multiple pairs have the same minimum difference, we return the one with the smallest values. If no such pair exists, we return `[-1, -1]`.

A simple approach would be to iterate through all numbers in this range, check whether each number is prime, store the primes, and then determine the pair with the smallest difference. However, checking if a number is prime requires verifying that it has no divisors other than `1` and itself. A naive way to do this is to test divisibility for all numbers up to `n`, but a more optimized approach would only check divisibility up to `sqrt(n)`. Even with this optimization, the approach remains too slow. Since `right` can be as large as $10^6$, iterating through all numbers and performing a divisibility check for each would still be inefficient, leading to a Time Limit Exceeded (TLE) error.

A much faster way to find all prime numbers up to a given limit is the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Instead of checking each number one by one, the sieve marks multiples of each prime in bulk, eliminating the need for repeated divisibility checks.  

We start with a list of numbers from 2 to 100. Notice we skip 1 since it’s not considered a prime. Starting with the smallest prime, 2, we know it’s prime because it hasn’t been marked yet. So, we keep it. Now, we cross out all multiples of 2 (like 4, 6, 8, etc.) because they’re definitely not prime. The next number that isn’t crossed out is 3, so we mark it as a prime. Then, we cross out all multiples of 3 (like 6, 9, 12, etc.). We keep going, finding the next unmarked number (which will be 5), and marking all of its multiples. We do this for 7 as well and continue until we’ve processed all numbers up to the limit.

The beauty of the Sieve of Eratosthenes is that it saves a lot of time by marking off composites in bulk, rather than testing each number individually to see if it’s prime. By the end, any number that’s still unmarked is a prime.

As we proceed, we collect all the numbers in an array `primeNumbers`, where `sieve[prime] = 1`. For any marked (non-prime) number, we could also keep track of the specific prime that marked it, though, for this problem, it’s sufficient to identify which numbers are prime.

Since all values lie between 1 and 1000000, we can iterate through the array, check for the minimum difference between two consecutive primes, and return it as the answer.

#### Algorithm

Main Function: `closestPrimes(int left, int right)`

1. Generate Prime Numbers using Sieve:
   - Create an integer array `sieve` of size `(right + 1)`, initialized to `1` (indicating prime numbers).
   - Set `sieve[0]` and `sieve[1]` to `0` (since `0` and `1` are not prime).
   - Iterate through numbers from `2` to `sqrt(right)`:
     - If the number is marked as prime (`sieve[number] == 1`), mark all its multiples as non-prime (`sieve[multiple] = 0`).

2. Collect Prime Numbers in Range:
   - Create a vector `primeNumbers` to store prime numbers within `[left, right]`.
   - Iterate through numbers from `left` to `right`:
     - If `sieve[num] == 1`, add `num` to `primeNumbers`.

3. Find the Closest Prime Pair:
   - If `primeNumbers.size() < 2`, return `{-1, -1}` (since there are not enough primes).
   - Initialize `minDifference` to the maximum integer value and `closestPair` to `{-1, -1}`.
   - Iterate through `primeNumbers` and check consecutive primes:
     - Compute `difference = primeNumbers[index] - primeNumbers[index - 1]`.
     - If `difference` is smaller than `minDifference`, update `closestPair = {primeNumbers[index - 1], primeNumbers[index]}`.

4. Return `closestPair` as the result.

Helper Function: `sieve(int upperLimit)`

1. Create an integer vector `sieve` of size `(upperLimit + 1)`, initialized to `1` (indicating prime numbers).
2. Set `sieve[0]` and `sieve[1]` to `0` (since `0` and `1` are not prime).
3. Iterate through numbers from `2` to `sqrt(upperLimit)`:
   - If `sieve[number] == 1`, mark all multiples of `number` as `0` (non-prime).
4. Return the `sieve` array.

#### Implementation#### Complexity Analysis

Let $R$ be `right` and $L$ be `left`, representing the range within which we search for prime numbers.

- Time Complexity: $O(R \log(\log(R)) + R - L)$

    The **Sieve of Eratosthenes** runs in $O(R \log(\log(R)))$, where $R$ is the upper limit of the sieve. After generating the sieve, iterating through the range $[L, R]$ to collect prime numbers takes $O(R - L)$. Finally, finding the closest prime pair requires $O(R - L)$ operations.

    Thus, the overall time complexity is $O(R \log(\log(R)) + R - L)$.

- Space Complexity: $O(R)$

    The algorithm uses a `sieve` array of size $O(R)$ to mark prime numbers. Additionally, the vector storing prime numbers within the range $[L, R]$ can have at most $O(R - L)$ elements. Thus, the overall space complexity is $O(R)$.

---

### Approach 2: Analyze Distance between twin primes

#### Intuition

To avoid storing the prime numbers while iterating through the range, we can check if the current number is prime or not. If it is, we can store it and take it's difference with the next prime that we find in this range. Observe that the **Sieve of Eratosthenes** approach cannot be used here, since it uses extra storage to check whether the number is prime or not. The only method left is to iterate through the divisors upto `sqrt(number)` and check if the current number is prime or not.

In this approach, we take advantage of a special property of prime numbers known as **twin primes**, which are pairs of prime numbers that differ by exactly `2`, such as `(3,5)`, `(11,13)`, and `(17,19)`. Instead of searching through all prime numbers, we can optimize our search by focusing on this pattern.  
A key mathematical observation under the given constraints (`1 ≤ L,R ≤ 10^6`) is that for any range `[L, R]` where `R - L ≥ 1452`, there is always at least one twin prime pair. This means that if the given range is wide enough (at least `1452` numbers long), we can be certain that a twin prime pair exists. Since no two prime numbers can be closer than a twin prime pair (which has a difference of exactly `2`), we can immediately return this result without further searching.You can use the following code snippet to verify this behavior by checking the maximum gap between consecutive prime numbers in the range [1, 10^6] (Click to expand):```cpp
vectorsieve(int upper_limit) {
    vectoris_prime(upper_limit + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int num = 2; num * num <= upper_limit; num++) {
        if (is_prime[num]) {
            for (int multiple = num * num; multiple <= upper_limit; multiple += num) {
                is_prime[multiple] = false;
            }
        }
    }
    return is_prime;
}
int main() {
    const int limit = 1000000;
    vectorprimes = sieve(limit);

    vectortwin_primes;
    // Collect all twin primes
    for (int num = 2; num <= limit - 2; num++) {
        if (primes[num] && primes[num + 2]) {
            twin_primes.push_back(num);
        }
    }
    int max_distance = 0;
    pairmax_twin_pair = {-1, -1};
    // Find the largest gap between consecutive twin primes
    for (int i = 1; i < twin_primes.size(); i++) {
        int distance = twin_primes[i] - twin_primes[i - 1];
        if (distance > max_distance) {
            max_distance = distance;
            max_twin_pair = {twin_primes[i - 1], twin_primes[i]};
        }
    }
    cout << "Twin primes with maximum distance: (" << max_twin_pair.first 
         << ", " << max_twin_pair.second << ")" << endl;
    cout << "Maximum twin prime distance: " << max_distance << endl;
    return 0;
}
```However, if the range `[L, R]` is smaller than 1452 numbers, we cannot rely on this property and must manually find the closest prime pair. To do this, we iterate through the numbers in the range, check which ones are prime, and compute the smallest difference between consecutive primes.  

Therefore, we leverage the concept of twin primes to optimize our search for the closest prime pair. Instead of storing all prime numbers and comparing them later, we track only the last encountered prime (`prevPrime`). As we iterate through the range `[left, right]`, if we find a new prime, we calculate the difference between it and `prevPrime`. If the difference is `2`, we instantly return the pair, since no closer pair can exist. This early exit significantly reduces unnecessary iterations, especially in large ranges where twin primes are guaranteed to exist. 

To summarize, if no twin prime pair is found initially, we continue searching for the closest prime pair by tracking the smallest difference encountered. However, if the range is greater than `1452`, it is mathematically guaranteed that at least one twin prime pair will exist within it.

#### Algorithm

Main Function: `closestPrimes(int left, int right)`

1. Initialize Variables:
   - `prevPrime`: Stores the last encountered prime number.
   - `closestA`, `closestB`: Stores the closest prime pair.
   - `minDifference`: Stores the minimum difference found (initialized to a large value).

2. Find the Closest Prime Pair in Range `[left, right]`:
   - Iterate through all numbers from `left` to `right`:
     - Use `isPrime(candidate)` to check if the number is prime.
     - If the number is prime:
       - If `prevPrime` is already set:
         - Calculate the difference between `prevPrime` and `candidate`.
         - If the difference is **2**, return `{prevPrime, candidate}` immediately (twin prime optimization).
         - If the difference is smaller than `minDifference`, update `closestA`, `closestB`, and `minDifference`.
       - Update `prevPrime` to `candidate`.

3. Handle Cases with Fewer Than 2 Primes:
   - If `closestA` is still `-1`, return `{-1, -1}`.

4. Return Result:
   - Return `{closestA, closestB}`.

Helper Function: `isPrime(int number)`

1. Handle Small Numbers:
   - If `number < 2`, return `false`.
   - If `number` is `2` or `3`, return `true` (both are prime).
   - If `number` is even and greater than `2`, return `false`.

2. Check for Divisibility:
   - Iterate from `3` to `√number`, checking only odd numbers.
   - If `number` is divisible by any of these, return `false`.

3. Return `true` if No Divisors Found.

#### Implementation#### Complexity Analysis

Let $R$ be `right` and $L$ be `left`, representing the range within which we search for prime numbers.

- Time Complexity: $O(\min(1452, R - L) \cdot sqrt(R))$  

  The algorithm iterates through numbers in the range `[L, R]` to identify prime numbers. For each number, it performs a primality check, which takes $O(\sqrt{R})$ time in the worst case.  

  - If `R - L ≥ 1452`, we know that a twin prime pair must exist in the range, allowing us to stop early. In this case, the algorithm processes at most 1452 numbers, leading to a complexity of $O(1452 \cdot \sqrt{R})$.  
  - If `R - L < 1452`, the algorithm checks up to `R - L` numbers, resulting in a worst-case complexity of $O((R - L) \cdot \sqrt{R})$.  

  Therefore, the overall time complexity is bounded by $O(\min(1452, R - L) \cdot \sqrt{R})$.

- Space Complexity: $O(1)$  

   We're only using a few variables that don't scale with the input size. Therefore, the overall space complexity remains $O(1)$.

---
