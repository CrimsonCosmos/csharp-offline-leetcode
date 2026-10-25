# 71. Simplify Path
**Difficulty:** Medium  
**Topics:** String, Stack
**Link (online only):** https://leetcode.com/problems/simplify-path/

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
The rules of a Unix-style file system are as follows:
The simplified canonical path should follow these rules:
Return the simplified canonical path.

**Example 1:**
```
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.
```

**Example 2:**
```
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.
```

**Example 3:**
```
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).
```

**Example 4:**
```
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.
```

**Example 5:**
```
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:
"..." is a valid name for a directory in this problem.
```

**Constraints:**
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.

