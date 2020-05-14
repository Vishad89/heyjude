#!/usr/bin/python3
"""

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
def maxProduct_subarray(arr):
    max_prod = 1
    min_prod = 1
    temp = 1
    final_max_prod = 1

    for i in range(len(arr)):
        if arr[i] > 0:
            max_prod = max_prod * arr[i]
            min_prod = min ( min_prod * arr[i], 1)
        elif arr[i] == 0:
            max_prod = 1
            min_prod = 1
        else: 
            temp = max_prod
            max_prod = max (min_prod * arr[i], 1)
            min_prod = temp * arr[i]

        if final_max_prod < max_prod:
            final_max_prod = max_prod
    
    return final_max_prod

def main():
    arr1 = [1, -2, -3, 0] 
    print("Maximum product subarray is", maxProduct_subarray(arr1)) 

main()