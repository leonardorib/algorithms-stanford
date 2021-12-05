import random

def _select(list, i, start, end):
	"""
	Finds the i-th smallest element

	Time complexity: Best case/Average = O(n) / Worst case = O(n^2)
	Space complexity: O(1)
	"""
	(pivot_index, pivot) = partition(list, start, end)

	if (pivot_index == i):
		return pivot
	elif (i > pivot_index):
		return _select(list, i, pivot_index + 1, end)
	elif (i < pivot_index):
		return _select(list, i, start, pivot_index - 1)

def select(list, i):
	return _select(list, i, 0, len(list) - 1)

def partition(list, start, end):
	"""
	Randomly selects an element of the array as pivot
	then rearrange the array such that every element to the left of the array
	is less than the pivot and every element to the right of the array is greater than the pivot
	"""
	# Randomly selects a pivot
	pivot_index = random.randint(start, end)
	pivot = list[pivot_index]

	# Moves pivot to the end
	list[end], list[pivot_index] = list[pivot_index], list[end]

	# Partition the array by comparing each element with the pivot
	i = start - 1
	for j in range(start, end):
		if (list[j] < pivot and i != j):
			i += 1
			list[i], list[j] = list[j], list[i]

	# Moves the pivot to it's correct position
	list[end] = list[i + 1]
	list[i + 1] = pivot

	return (i + 1, pivot) # Pivot index / Pivot

def test_select():
	print("Running tests...")
	passed = True
	for _ in range(1000):
		list_size = random.randint(2, 1500)
		test_list = random.sample(range(1,2000), list_size)
		desired_position = random.randint(0, list_size - 1)
		found_element = select(test_list, desired_position)
		sorted_list = sorted(test_list)
		expected_element = sorted_list[desired_position]
		if (found_element != expected_element):
			passed = False
			break
	if(passed):
		print("PASSED select")
	else:
		print("--> FAILED select")

test_select()
