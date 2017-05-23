def insort(arr):

		for i in range(1, len(arr)):
			 j = i
			 while j > 0 and (arr[j-1] > arr[j]):
			 	arr[j], arr[j-1] = arr[j-1], arr[j]
			 	print arr
			 	j = j-1


def userarr():

		arr1 = []
		elem = int(raw_input("insert how many elements you want:"))
		for i in range(0, elem):
    			arr1.append(int(raw_input("Enter next no :")))
			print arr1

insort(arr1)
