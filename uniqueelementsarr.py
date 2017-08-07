# find unique numbers from two arrays
# This is very close to missingelements.py solution, but with a slight change

from  collections import defaultdict

def uniqueelementsarr (arr1,arr2):
	uniquenums = []
	dict = defaultdict(int)
	for num in  arr1 + arr2:
		dict[num] += 1

	for num in dict:
		if dict[num] == 1:
			uniquenums.append(num)
	return uniquenums



a = [1, 4, 5, 6,7 ,2, 45, 78, 5 ,"abc", "sha"]
b = [1, 5, 6, 7, 45, 2, 42, 1, 4, "abc"]
print uniqueelementsarr(a, b)