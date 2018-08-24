#!/usr/bin/python

""" 
This function takes the name of a directory 
and prints out the paths files within that 
directory as well as any files contained in 
contained directories.
"""

import sys
import os

def print_directory_contents(spath):

    for sChild in os.listdir(spath):
        sChildPath= os.path.join(spath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


def main():
    #path=sys.argv[1]
    print_directory_contents(sys.argv[1])
    #print path



if __name__=='__main__':
    main()

