import random

def partition(list, start, end):
	"""
	Randomly selects an element of the array as pivot
	then rearrange the array such that every element to the left of the array
	is less than the pivot and every element to the right of the array is greater than the pivot
	"""
	# Randomly selects a pivot
	pivotIndex = random.randint(start, end)
	pivot = list[pivotIndex]

	# Moves pivot to the end
	list[end], list[pivotIndex] = list[pivotIndex], list[end]

	# Partition the array by comparing each element with the pivot
	i = start - 1
	for j in range(start, end):
		if (list[j] < pivot and i != j):
			i += 1
			list[i], list[j] = list[j], list[i]

	# Moves the pivot to it's correct position
	list[end] = list[i + 1]
	list[i + 1] = pivot

	return i + 1 # Pivot index

def quick_sort(list, start, end):
	"""
	Recursevely sorts an array of numbers
	Time complexity: Best case/Average = O(n*logn) / Worst case = O(n^2)
	Space complexity: O(1)
	"""
	if (start < end):
		pivotIndex = partition(list, start, end)

		quick_sort(list, start, pivotIndex - 1)
		quick_sort(list, pivotIndex + 1, end)

		return list

def test_quick_sort():
	print("Running tests...")
	passed = True
	for _ in range(100):
		test_list = random.sample(range(1,2000), random.randint(2, 1500))
		expected_sorted = sorted(test_list)
		quick_sort(test_list, 0, len(test_list) - 1)
		if (test_list != expected_sorted):
			passed = False
			break
	if(passed):
		print("PASSED quick_sort")
	else:
		print("--> FAILED quick_sort")

test_quick_sort()
