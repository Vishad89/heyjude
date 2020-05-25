"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

def minimnum_window_substring(str,sub):
    start = 0
    end = 2
    min = 0
    sub = list(sub)
    while end <= len(str):
        print(str[start:end])
        while sub in str[start:end]:
            min = end - start
            start += 1
        end += 1
    return min
print(minimnum_window_substring("ADOBECODEBANC","ABC"))