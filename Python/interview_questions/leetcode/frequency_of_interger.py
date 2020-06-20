#!/usr/bin/python3

"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
def search_freq_num(arr,num):
    left,right  = -1, -1
    l, r = 0, len(arr)-1
    # find the left index of the num 
    while l < r:
        m = (l+r)//2
        if arr[m] < num:
            l = m + 1
        else: 
            r = m
    if arr[l] != num:
        return -1
    left = l

    # find the right index of the num
    l , r = left,len(arr) - 1
    while l < r:
        m = (l+r)//2 + 1
        if arr[m] > num:
            r = m -1
        else: 
            l = m
    right = r

    return  (right -left +1)

a = [1,2,3,3,3,4,4,4,5,5,6]
print(search_freq_num(a,6))

    

    