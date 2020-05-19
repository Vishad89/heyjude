#!/usr/bin/python
"""
Reverse the order of words in a given sentence (an array of characters)

example:
The "Hello World" string reversed should be "World Hello".
"""
import re

def reverse_words1(str):
    words = re.findall('\w+|[! : , . ? ` ~ " ]', str)
    special_char = '!:,.?`~"'
    i = 0
    j = len(words) - 1
    while i <= j:
        while (words[i] in special_char):
            i += 1
        while (words[j] in special_char):
            j -= 1
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1
    print(''.join(words))

reverse_words1("Hello, World!")
