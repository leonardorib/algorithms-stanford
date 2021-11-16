# Counting inversions problem
# Input: array A containing numbers 1, 2, 3, ..., n in some arbitrary order.
# Output: number of inversions = number of pairs (i,j) of array indices with i < j and A [i] > A[j]

# This is implementation is based on the merge sort algorithm.
# With some slightly modifications is possible to calculate
# the number of inversions on a list in O(n*log(n)) time (as in merge sort)

# Merges and count the number only of split inversions
# between two already sorted lists
def merge_and_count_split_inv(A, B):
	C = [0]*(len(A) + len(B))
	i = 0
	j = 0
	k = 0
	split_inversions = 0
	while (i < len(A) and j < len(B)):
		if (A[i] <= B[j]):
			C[k] = A[i]
			i = i + 1
		else:
			C[k] = B[j]
			j = j + 1
			split_inversions = split_inversions + (len(A) - i)
		k = k + 1

	while (i < len (A)):
		C[k] = A[i]
		i = i + 1
		k = k + 1

	while (j < len (B)):
		C[k] = B[j]
		j = j + 1
		k = k + 1
	return (C, split_inversions)

# Sorts and counts inversions
def sort_and_count_inv(list):
	 # Base case
	if (len(list) <= 1):
		return (list, 0)

	middle = len(list) // 2

	A = [0]*(middle)
	B = [0]*(len(list) - middle)

	for i in range(0, middle):
		A[i] = list[i]
	for i in range(middle, len(list)):
		B[i - len(list)] = list[i]

	(A, count_A) = sort_and_count_inv(A)
	(B, count_B) = sort_and_count_inv(B)

	(C, count_split_inv) = merge_and_count_split_inv(A, B)
	return (C, count_A + count_B + count_split_inv)

def test_sort_and_count_inv(list, expected_count):
	(list, count) = sort_and_count_inv(list)
	if (count == expected_count and list == sorted(list)):
		print("sort_and_count_inv PASSED - Inversions:", count)
	else:
		print("---> sort_and_count_inv FAILED - Inversions:", count, "Expected: ", expected_count)

test_sort_and_count_inv([], 0)
test_sort_and_count_inv([1], 0)
test_sort_and_count_inv([2, 4, 1, 3, 5], 3)
test_sort_and_count_inv([2, 3, 4, 5, 6], 0)
test_sort_and_count_inv([10, 10, 10], 0)
test_sort_and_count_inv([1,2,3,1,2], 3)
test_sort_and_count_inv([22,16,15,7,2,1], 15)
test_sort_and_count_inv([1, 20, 6, 4, 5], 5)