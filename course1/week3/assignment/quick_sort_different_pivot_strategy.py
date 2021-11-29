"""
    Author: Leonardo Ribeiro
    Python Version: 3.8.10
"""
import random
import os
from typing import Literal

# Type definitions
PivotMethod = Literal["from_start", "from_end", "median_of_three"]

# Global variable to store the number of comparisons made
comparisons = 0

def partition(list, start, end, pivot_method: PivotMethod):
	# Counting comparisons made
	global comparisons
	length = end - start + 1
	comparisons  += (length - 1)

	## Selects pivot based on the method specified
	pivot = 0
	pivot_index = 0
	if (pivot_method == "from_start"):
		pivot_index = start
		pivot = list[start]
	elif (pivot_method == "from_end"):
		pivot_index = end
		pivot = list[end]
	elif (pivot_method == "median_of_three"):
		middle = start + (length // 2)
		if (length % 2 == 0):
			middle = middle -1
		p_candidates = {start: list[start], middle: list[middle], end: list[end]}
		p_candidates.pop(min(p_candidates, key=p_candidates.get))
		pivot_index = min(p_candidates, key=p_candidates.get)
		pivot = list[pivot_index]

	# Positioning pivot at the beginning of the list
	list[start], list[pivot_index] = list[pivot_index], list[start]

	# Main partition logic
	i = start + 1
	for j in range(start, end + 1):
		if (list[j] < pivot):
			list[j], list[i] = list[i], list[j]
			i += 1
	# Moving pivot to it's correct position
	list[start], list[i - 1] = list[i - 1], list[start]
	return i - 1 # Pivot index

def quick_sort(list, start, end, pivot_method: PivotMethod):
	if (start < end):
		pivotIndex = partition(list, start, end, pivot_method)

		quick_sort(list, start, pivotIndex - 1, pivot_method)
		quick_sort(list, pivotIndex + 1, end, pivot_method)

def get_list_from_file():
	"""
	Utility function to get input array from .txt file
	"""
	filepath = os.path.join(os.path.dirname(__file__),"_32387ba40b36359a38625cbb397eee65_QuickSort.txt")
	with open(filepath) as file:
		input_list = [int(line) for line in file]
	return input_list

def run_with_assignment_input():
	"""
	Runs the code with the assignment input, test correctness and print the number of comparisons
	"""
	global comparisons
	print("--- Running with assignment input... ---")
	input = get_list_from_file()
	expected_sorted = sorted(input)

	comparisons = 0
	quick_sort(input, 0, len(input) - 1, "from_start")
	if (expected_sorted == input):
		print("PASSED - Correctness of quick_sort with pivot from start")
		print("Comparisons pivot from start: ", comparisons)
	else:
		print("--> FAILED - Correctness of quick_sort with pivot from start")
	print()

	comparisons = 0
	input = get_list_from_file()
	quick_sort(input, 0, len(input) - 1, "from_end")
	if (expected_sorted == input):
		print("PASSED - Correctness of quick_sort with pivot from end")
		print("Comparisons pivot from end: ", comparisons)
	else:
		print("--> FAILED - Correctness of quick_sort with pivot from end")
	print()

	comparisons = 0
	input = get_list_from_file()
	quick_sort(input, 0, len(input) - 1, "median_of_three")
	if (expected_sorted == input):
		print("PASSED - Correctness of quick_sort with pivot as median_of_three")
		print("Comparisons median_of_three: ", comparisons)
	else:
		print("--> FAILED - Correctness of quick_sort with pivot as median_of_three")
	print()

def test_quick_sort():
	"""
	Tests with multiple random inputs to ensure robustness
	"""
	print("--- Running tests with random inputs... ---")
	passed = True
	for _ in range(100):
		test_list = random.sample(range(1,2000), random.randint(2, 1500))
		expected_sorted = sorted(test_list)
		quick_sort(test_list, 0, len(test_list) - 1, "from_start")
		if (test_list != expected_sorted):
			passed = False
			break
	if(passed):
		print("PASSED quick_sort with pivot from start")
	else:
		print("--> FAILED quick_sort with pivot from start")

	passed = True
	for _ in range(100):
		test_list = random.sample(range(1,2000), random.randint(2, 1500))
		expected_sorted = sorted(test_list)
		quick_sort(test_list, 0, len(test_list) - 1, "from_end")
		if (test_list != expected_sorted):
			passed = False
			break
	if(passed):
		print("PASSED quick_sort with pivot from end")
	else:
		print("--> FAILED quick_sort with pivot from end")

	passed = True
	for _ in range(100):
		test_list = random.sample(range(1,2000), random.randint(2, 1500))
		expected_sorted = sorted(test_list)
		quick_sort(test_list, 0, len(test_list) - 1, "median_of_three")
		if (test_list != expected_sorted):
			passed = False
			break
	if(passed):
		print("PASSED quick_sort with pivot as median of three")
	else:
		print("--> FAILED quick_sort with pivot as median of three")
	print()


def main():
	test_quick_sort()
	run_with_assignment_input()

main()

# Expected comparisons number:
# quick_sort_pivot_start: 162085
# quick_sort_pivot_end: 164123
# quick_sort_pivot_median_of_three: 138382
