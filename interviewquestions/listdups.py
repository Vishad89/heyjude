# Remove duplicate elemets from a list

def find_dups(arr):
	uq = []
	l = len(arr)
	print l
	for i in range(len(arr)):
		print i
		if arr[i] in uq:
			pass
		else:
			uq.append(arr[i])
	print uq


a = [1,2,3,"a",5,"c","f",2,3,4,"q","a"]
find_dups(a)
