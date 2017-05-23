def sort(arr):

		for i in range(len(arr)):
			for j in range(len(arr) - 1 - i):
				if (arr[j] > arr[j+1]):
					arr[j], arr[j + 1] = arr[j +1 ], arr[j]
				else:
					print arr


arr1 = [5, 8, 35, 789, 900, 4173472, 1, 4, 3, 2, 10, 6, 7]
sort(arr1)
