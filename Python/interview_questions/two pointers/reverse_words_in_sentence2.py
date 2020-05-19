"""
Reverse the order of words in a given sentence (an array of characters)

example:
The "Hello World" string reversed should be "World Hello".

In This approach, I am trying to reverse the string completely (including punctuations) first and then reverse them back word by word. 

"""
import re
import sys

def str_rev(str, start, end):
    if len(str) is None or len(str) < 2:
        return
    while start < end:
        temp = str[start]
        str[start] = str[end]
        str[end] = temp
        start += 1
        end -= 1
   

def reverse_words_in_sentence(sentence):
    sentence = list(sentence)
    str_len = len(sentence)
    str_rev(sentence, 0, str_len-1)

    start = 0
    end = 0
    while True:
        while start < str_len and sentence[start] == ' ':
            start += 1
        if start == str_len:
            break
        
        end = start + 1
        while end < str_len and sentence[end] != ' ':
            end += 1
        str_rev(sentence, start, end-1)
        start = end
    return("".join(sentence))


if __name__ == "__main__":
        sentence = input("please input any string here, it can be a sentence too: ")
        print("string : ", sentence)
        sentence = reverse_words_in_sentence(sentence)
        print("string reversed : ", sentence)