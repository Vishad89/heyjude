def maxnum(arr):
	m=arr[0]
	for num in arr:
	    if num > m:
	        m=num
	print(m)


def arrcrt():

	arr = []
	elem = int(raw_input("insert how many elements you want:"))
	for i in range(0, elem):
    		arr.append(int(raw_input("Enter next no :")))
	print arr
	maxnum(arr)
arrcrt()
