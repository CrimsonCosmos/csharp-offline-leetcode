# 535. Encode and Decode TinyURL
**Difficulty:** Medium  
**Topics:** Hash Table, String, Design, Hash Function
**Link (online only):** https://leetcode.com/problems/encode-and-decode-tinyurl/

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
Implement the Solution class:

**Example 1:**
```
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
```

**Constraints:**
- 1 <= url.length <= 104
- url is guranteed to be a valid URL.

