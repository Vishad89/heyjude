#!/usr/bin/python3
from random_word import RandomWords
import random

def master_guess(str,str_in):
    i,count = 0,0
    while i < min(len(str),len(str_in)):
        if str[i] == str_in[i]:
            count += 1
        else:
            pass
        i += 1
    return count 

def main():    
    r = RandomWords()
    rand = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", maxLength=8, limit=5)
    print(rand)
    str = random.choice(rand)
    str_in = ''
    j = 0
    while j < len(rand)//2 or str_in == str:
        str_in = input("guess the word: ")
        result = master_guess(str, str_in)
        if result == len(str):
            print("nailed it")
            return 0
        elif result < len(str)//2:
            print("try harder")
        else:
            print("very close, keep trying")
        j +=1
    print("the word was: ", str)

main()