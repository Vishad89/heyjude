#!/usr/bin/python3
"""
Given a sorted array, ignores duplicates and outputs length of the array

Example:
array = [ 1, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8 ]

Output:
7
"""
def removeDuplicates(arr):
    i = 0 
    for j in range(1, len(arr) -1 ):
        if arr[i] == arr[j]:
            continue
        else: 
            i += 1
            arr[i] = arr[j]
    return i + 1

#print(removeDuplicates([1,1,3,4,5,6,6]))