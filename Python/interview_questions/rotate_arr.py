#! /usr/bin/python3
"""

Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

"""

#method1: pop and insert
def rotate(arr, k):
    i = 0
    
    #if k is greater than the array length
    k = k % len(arr)

    while i < k:
        arr.insert(0,arr.pop())
        i += 1
    return arr

print(rotate([1,2,3,4,5,6,7],3))

#method2: deque and append
from collections import deque

def rotate_new(arr,k):
    d = deque(arr)
    i = 0
    k = k % len(arr)
    while i < k:
        d.appendleft(d.pop())
        i += 1
    arr = list(d)
    print(arr)

rotate_new([1,2,3,4,5,6,7],3)