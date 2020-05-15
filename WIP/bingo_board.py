#! /usr/bin/python

import numpy as np
import random
import time

def generaterandomnumbers():
    #num_pot = np.arange(1,91)).reshape(9,10)
    num_pot = np.zeros([9,10], dtype=int)
    housie_pot = [k for k in range(1,91)]
    while len(housie_pot) > 0:
        x = str(housie_pot.pop(random.randrange(len(housie_pot))))
        if len(x) == 1:
            i = 0
            j = x
        elif int(x)%10 == 0:
            i = int(x)/10 - 1
            j = 10 
        else:
            j = x[1]
            i = x[0]
        num_pot[int(i)][int(j)-1] = int(x)
        print('\033[1;31m', x,'\033[1;m',"\n\n",num_pot,"\n\n")
        input("Press Enter for next number... \n")
        #time.sleep(15)

# def random_numbers():
#     i = random.randint(0,9)
#     j = random.randint(0,9)
#     while [i,j] not in x:
#        i = random.randint(0,9)
#        j = random.randint(0,9) 
#        x.append([i,j])
#     print(x)

# random_numbers()
generaterandomnumbers()