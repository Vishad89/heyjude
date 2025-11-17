#!/usr/bin/python3

"""
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

def squared_sorted_array(arr):
    left = 0 
    right = len(arr) - 1
    result = []

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] * arr[left])
            left += 1
        else:
            result.append(arr[right] * arr[right])
            right -= 1

    return result[::-1]

arr1 = [ -17, -16, -5, 0, 4, 6, 20]
print(squared_sorted_array(arr1))