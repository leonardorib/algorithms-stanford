"""
    Author: Leonardo Ribeiro
    Python Version: 3.8.10
"""

# For testing purposes
import random

def merge(A, B):
	"""
	Merge two sorted lists into one sorted list
	"""
	C = [0]*(len(A) + len(B))

	i = 0
	j = 0
	k = 0

	while (i < len(A) and j < len(B)):
		if (A[i] < B[j]):
			C[k] = A[i]
			i = i + 1
		else:
			C[k] = B[j]
			j = j + 1
		k = k + 1

	"""
	i and j are not zero at this point,
	So the last two loops only execute for the remaining elements
	in case of one list is "complete" and the other is not.
	"""
	while (i < len (A)):
		C[k] = A[i]
		i = i + 1
		k = k + 1

	while (j < len (B)):
		C[k] = B[j]
		j = j + 1
		k = k + 1
	return C

def merge_sort(list):
	"""
	Sorts a list of numbers
	"""

	 # Base case
	if (len(list) <= 1):
		return list

	middle = len(list) // 2

	A = [0]*(middle)
	B = [0]*(len(list) - middle)

	for i in range(0, middle):
		A[i] = list[i]
	for i in range(middle, len(list)):
		B[i - len(list)] = list[i]

	A = merge_sort(A)
	B = merge_sort(B)

	C = merge(A, B)
	return C

def test_merge_only(A, B):
	"""
	Tests merge operation
	"""
	result = merge(A, B)
	expected_result = sorted([*A, *B])
	if (result == expected_result):
		print("PASSED Merge operation - Result:", result)
	else:
		print("--> FAILED Merge operation - Result: ", result, "  Expected: ", expected_result)

def test_merge_sort(list):
	"""
	Tests merge sort implementation
	"""
	result = merge_sort(list)
	expected_result = sorted(list)
	if (result == expected_result):
		print("PASSED Merge Sort - Result:", result)
	else:
		print("--> FAILED Merge Sort - Result: ", result, "  Expected: ", expected_result)

# Running tests

test_merge_only([1,3,5], [2,4,9,11])
test_merge_only([1,3,5,22,22,102,106], [2,4,9,11,45,65,109,152])

test_merge_sort([1,3,5,22,22,102,106,2,4,9,11,45,65,109,152])
test_merge_sort(random.sample(range(1,200), 53))
