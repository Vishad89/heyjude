#!/usr/bin/python3

"""
write a function that return sorted array containing the squares of the intergers in a sorted array

example:

array1 = [ -6, -4. 1, 2, 3, 7 ]

output: 
[ 1, 4, 9, 16, 36, 49 ]
"""

def squared_sorted_array(arr):
    left = 0 
    right = len(arr) - 1
    result = [ 0 for x in arr]

    for i in range(len(arr)-1, 0, -1):
        if abs(arr[left]) > abs(arr[right]) :
            result[i] = arr[left] * arr[left]
            left += 1
        else:
            result[i] = arr[right] * arr[right]
            right -= 1

    return result

def main():
    arr1 = [ -17, -16, -5, 0, 4, 6, 20]
    print(squared_sorted_array(arr1))

main()