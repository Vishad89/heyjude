#Given these two arrays, find which element is missing in the second array. 

from collections import defaultdict


def missingelementsarr(arr1, arr2):
	dict = defaultdict(int)
	arr1.sort()
	arr2.sort()
	uniknums = []

	for num in b:
		dict[num] += 1
	for num in a:
		if dict[num] == 0:
			uniknums.append(num)
		else: 
			dict[num] +=1
	return uniknums


a = [1, 4, 5, 6,7 ,2, 45, 78, 5, 66]
b = [1, 5, 6, 7, 45, 2, 78]
print missingelementsarr(a,b)