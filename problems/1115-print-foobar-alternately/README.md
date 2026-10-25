# 1115. Print FooBar Alternately
**Difficulty:** Medium  
**Topics:** Concurrency
**Link (online only):** https://leetcode.com/problems/print-foobar-alternately/

Suppose you are given the following code:
The same instance of FooBar will be passed to two different threads:
Modify the given program to output "foobar" n times.

**Example 1:**
```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```

**Example 2:**
```
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
```

**Example 3:**
```
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
```

**Constraints:**
- 1 <= n <= 1000

