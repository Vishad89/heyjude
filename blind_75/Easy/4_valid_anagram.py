"""

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

# class Solution:
#     def counters(strg):
#         counters = {}
#         for s in strg:
#            if s in counters:
#                counters[s] += 1
#            else:
#                 counters[s] = 1
#         return counters

    
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) is not len(t):
#             return False
#         s_counter = Solution.counters(s)
#         t_counter = Solution.counters(t)
#         return(s_counter == t_counter) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
            
        
    
s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

o = Solution()
print(o.isAnagram(s1,t1))
print(o.isAnagram(s2,t2))

