#Given an integer array, output all pairs that sum up to a specific value k.

def pairsumarray2(arr, k):
	set(arr)
	for num in arr:
		diff = k - num
		arr.remove(num)
		if diff in arr:
			return (num,diff)


a = [1, 7, 8, 7, 11, 3, 80]
print pairsumarray2(a, 14)
