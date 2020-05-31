#!/usr/bin/python3

# Assumption: sorted array


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    result = False

    while (first <= last and result == False):
        mid = (first + last) // 2
        if array[mid] == item:
            result = True
        else:
            if item < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return result 

print(binary_search([1,2,3,4,5,6,10,21,23,40,111], 2221))