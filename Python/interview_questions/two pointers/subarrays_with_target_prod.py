#!/usr/bin/python3
"""
 Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
"""
from collections import deque

def find_subarray_with_target_prod(arr, target_prod):
    left = 0 
    right = 0
    temp_prod = 1
    result = []

    for right in range(len(arr) - 1):
        temp_prod *= arr[right]
        while (temp_prod >= target_prod and left < len(arr)):
                temp_prod /= arr[left]
                left += 1
        temp_list = deque()
        for i in range(right, left - 1, -1):
                temp_list.appendleft(arr[i])
                result.append(list(temp_list))
    return result

def main():
    print(find_subarray_with_target_prod([2, 5, 3, 10], 30))
    print(find_subarray_with_target_prod([8, 2, 6, 5], 50))	

main()

