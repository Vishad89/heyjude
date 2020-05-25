"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

def anagram_check(s,t):
    if len(s) is not len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    else:
        return False

s=input("string1: ")
t=input("string2: ")
r = anagram_check(s,t)
if r is True:
    print ("Noice! ")
else:
    print ("oO")



