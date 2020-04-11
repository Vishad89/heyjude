#/usr/bin/python3
"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""
def find_averages_of_subarrays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i , i + k):
            _sum += arr[j]
        result.append(_sum/k)
    return result 

def main():
    arr1 = [ 1, 3, 2, 6, -1, 4, 1, 8, 2 ]
    K = 4
    result = find_averages_of_subarrays(K, arr1)
    print("averages of subarray of size " + str(K)  +" : " + str(result))

main()