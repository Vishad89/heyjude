"""
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
            slow, fast, n = 0, -1, len(s)
            d = {'a':0, 'b':0, 'c':0}
            res = 0
            
            while slow < n or fast < n:
                if min(d.values()) >= 1:
                    d[s[slow]] -= 1
                    slow += 1
                while min(d.values()) < 1:
                    if fast < n-1:
                        fast += 1
                        d[s[fast]] += 1
                    else:
                        return res
                res += n - fast

s = Solution()
print(s.numberOfSubstrings("abcabc"))