#Largest Continuous Sum
#Given an array of integers (positive and negative) find the largest continuous sum.


def largestcontsum(arr):
	
	if len(arr) == 0:
		return

	currentSum = maxSum = int(arr[0])
	print currentSum, maxSum

	for num in arr[1:]:
		print num, currentSum + num, currentSum
		currentSum = max(num, currentSum+num)
		maxSum = max(currentSum, maxSum)
		print maxSum
	
	return maxSum


print largestcontsum([-1, -5, -2, -6, -7, -9, -5])