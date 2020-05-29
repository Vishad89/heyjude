"""
How it works:
1) Convert it into a maxheap (parent node >= child node)
once that is done and tree satisfies the maxheap condition, which is, the largest item is stored at the root elment...

2) Swap root element with the last indexed element 
3) remove the swapped last element from heap, so reduce the heap size by 1
4) heapify the array again, to get the largest element from the rest at the root
5) repeart the from 2...
"""

def heapify(arr, n, i):

    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[i]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,n,largest)
    
def heapsort(arr):
    n = len(arr)
    
    # 1. implement maxheap 
    # could work with n//2-1 but n//2 is for the safer version, 
    # range is set that way that it can start from the lowest parent node
    for i in range(n//2, -1,-1):
        heapify(arr,n,i)

    # Step 2 ... 4
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
        print(arr)
    return arr

arr1 = [1,12,9,5,6,10,50,50,411]
print(heapsort(arr1))

