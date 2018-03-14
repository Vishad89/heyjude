"""
    Bubble Sort
    -----------
    A naive sorting that compares and swaps adjacent elements.
    
    Time Complexity: O(n**2)
    
    Space Complexity: O(1) Auxiliary
    
    http://en.wikipedia.org/wiki/Bubble_sort

"""

def bubblesort(arr):

	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr


arr1 = [5, 8, 35, 789, 900, 4173472, 1, 4, 3, 2, 10, 6, 7]
bubblesort(arr1)
