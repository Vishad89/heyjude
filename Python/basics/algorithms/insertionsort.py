# Insertion sort with User input array

"""
    Insertion Sort
    --------------
    A sort that uses the insertion of elements in to the list to sort the list.
    
    Time Complexity: O(n**2)
    
    Space Complexity: O(n) total
   
"""
def insertionsort(arr):

	for i in range(len(arr):
		j = i 
		while j > 0 and arr[j-1] > arr[j]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
		    j = j-1
    return arr


arr1 = [8,4,1,2,5]
insertionsort(arr1)
