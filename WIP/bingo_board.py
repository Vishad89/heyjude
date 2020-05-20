#! /usr/bin/python

import numpy as np
import random
import time

def housie_numbers():
    # two lists 
    # This is where numbers will be populated
    housie_board = np.zeros([9,10], dtype=int)
    #housie_board = np.empty([9,10], dtype=int)
    # This is where numbers will be drawn from 
    numbers_pot = [k for k in range(1,91)]
    
    # run until we run out of numbers to draw out from number_pot
    while len(numbers_pot) > 0:
        x = numbers_pot.pop(random.randrange(len(numbers_pot)))
        if x < 10:
            i = 0
            j = x
        elif x%10 == 0:
            i = x/10 -1
            j = 10
        else:
            i = x/10
            j = x%10
        housie_board[int(i)][int(j)-1] = x
        print('\033[0.5;31m', x,'\033[2;m',"\n\n",'\033[1;32m', housie_board,'\033[2;m',"\n\n")
        print(input("Press Enter for next number... \n"))
    
housie_numbers()
