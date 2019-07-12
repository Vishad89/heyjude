#Given an integer array, output all pairs that sum up to a specific value k.

def pairsumarray(arr, k):
	if len(arr) < 2:
		return arr
	arr.sort()
	pairs=[]
	#print arr
	left = 0 
	right = len(arr)-1
	while left < right:
		sum = arr[left] + arr[right]
		if sum == int(k):
			pairs.append((arr[left], arr[right]))
			left += 1
		elif sum < int(k):
			left += 1
		else:
			right -= 1
	print "Pairs, which sums up to k are ", pairs

arr1 = [ 1, 8, 11, 15, 6, 7, 18, 20 , 25]
num = raw_input("any number: ")
pairsumarray(arr1, num)
