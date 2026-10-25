# 831. Masking Personal Information
**Difficulty:** Medium  
**Topics:** String
**Link (online only):** https://leetcode.com/problems/masking-personal-information/

You are given a personal information string s, representing either an email address or a phone number. Return the masked personal information using the below rules.
Email address:
An email address is:
To mask an email:
Phone number:
A phone number is formatted as follows:
To mask a phone number:

**Example 1:**
```
Input: s = "LeetCode@LeetCode.com"
Output: "l*****e@leetcode.com"
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
```

**Example 2:**
```
Input: s = "AB@qq.com"
Output: "a*****b@qq.com"
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.
```

**Example 3:**
```
Input: s = "1(234)567-890"
Output: "***-***-7890"
Explanation: s is a phone number.
There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
Thus, the resulting masked number is "***-***-7890".
```

**Constraints:**
- s is either a valid email or a phone number.
- If s is an email:
	
8 <= s.length <= 40
s consists of uppercase and lowercase English letters and exactly one '@' symbol and '.' symbol.
- 8 <= s.length <= 40
- s consists of uppercase and lowercase English letters and exactly one '@' symbol and '.' symbol.
- If s is a phone number:
	
10 <= s.length <= 20
s consists of digits, spaces, and the symbols '(', ')', '-', and '+'.
- 10 <= s.length <= 20
- s consists of digits, spaces, and the symbols '(', ')', '-', and '+'.

