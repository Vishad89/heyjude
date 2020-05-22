#!/usr/bin/python3
"""
In a sorted array remove second duplicate and return array length

Example:

arr = [ 0, 0, 1, 1, 1, 2 ]
output:
5

as new array would become 
arr = [ 0, 0, 1, 1, 2 ]

"""
import sys

def removeDuplicatesSecond(arr):
    read_pos = 2
    wrtie_pos = 2
    #print(arr)
    while read_pos < len(arr):
        if arr[read_pos] != arr[wrtie_pos-2]:
            arr[wrtie_pos] = arr[read_pos]
            wrtie_pos += 1
        read_pos += 1
        print(arr,wrtie_pos,read_pos)
    arr[wrtie_pos] = '\0'
    print(arr,wrtie_pos,read_pos)
    print_array(arr)

def print_array(s):
  i = 0
  while i < len(s) and str(s[i]) != '\0' :
    sys.stdout.write(str(s[i]))
    i += 1
  print()
    
def main():
    #a = [0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10]
    b = [0, 1, 1, 1, 2, 3, 5, 5, 5, 6]
    removeDuplicatesSecond(b)

main()

