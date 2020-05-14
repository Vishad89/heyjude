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

def removeDuplictesAfterSecond(arr):
    i = 0 
    repeat = 1
    print(arr)
    for j in range(1, len(arr)-1):
        if arr[i] != arr[j]:
            repeat = 1
            i += 1
            arr[i] = arr[j]
        if arr[i] == arr[j] and repeat >= 2:
            repeat += 1
            continue
        elif arr[i] == arr[j] and repeat < 2:
            repeat += 1
            i += 1
    print(arr)


def main():
    a = [0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10]
    b = [0, 1, 1, 1, 2, 3, 5, 5, 5, 6]
    return removeDuplictesAfterSecond(a)

main()
