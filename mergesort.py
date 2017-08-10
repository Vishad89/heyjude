# Merge sort


def merge(left, right):
	"""Compares and Merges arrays."""

	left_index, right_index = 0, 0
	result = []
	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1

	result += left[left_index:]
	result += right[right_index:]
	return result

def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)



a = [17,2,4,3, 444, 5546, 7, 6, 63, 2, 5,6 ,7 ,77,15,10]
print merge_sort(a)
