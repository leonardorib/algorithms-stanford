import math
from strassen import strassen, zeros_matrix

def main():
	run_multiplication_tests()

# Strassen's Algorithm for matrix multiplication - Generalization for any input

# If inputs are not power of two, adds zeros to matrices, runs Strassen's
# algorithm and then extract the result without the extra zero padding

# For the base implementation of Strassen's Algorithm, see strassen.py
def strassen_generalized(a, b):
	m = len(a)
	n = len(a[0])
	p = len(b[0])

	if (n != len(b)):
		raise Exception("Matrices cannot be multiplied")

	[a, b] = pad_with_zeros_until_power_of_two(a, b)

	result = strassen(a, b)

	return extract_result_without_zero_padding(result, m, p)

# Runs tests
def run_multiplication_tests():
	test_strassen_generalized_multiply(
		[
			[1, 2, 3],
			[4, 5, 6]
		],
		[
			[7, 8],
			[9, 10],
			[11, 12]
		],
		[
			[58, 64],
			[139, 154]
		]
	)

## BASIC OPERATIONS

# Complete matrix with zeros until it's n*n and n is a power of two
def pad_with_zeros_until_power_of_two(m1, m2):
	max_dimension = max(len(m1), len(m1[0]), len(m2), len(m2[0]))
	n = find_next_power_of_two(max_dimension)
	m1 = make_matrix_square(m1, n)
	m2 = make_matrix_square(m2, n)
	return [m1, m2]

# Extracts upper left of the matrix in case it's zero padded
def extract_result_without_zero_padding(matrix, rows, cols):
	result = zeros_matrix(rows, cols)
	for i in range(rows):
		for j in range(cols):
			result[i][j] = matrix[i][j]
	return result


## HELPER METHODS

# Find the next integer that is a power of two
def find_next_power_of_two(x):
	x = int(x)
	while (not math.log(x, 2).is_integer()):
		x = x + 1
	return x

# Prints a matrix
def print_matrix(m):
	for i in range(len(m)):
		print(m[i])

# Adds a columns filled with zeros at the matrix right
def add_zeros_columns(matrix, cols_number):
	for i in range(len(matrix)):
		for n in range(cols_number):
			matrix[i].append(0)
	return matrix

# Adds a row filled with zeros at the matrix bottom
def add_zeros_rows(matrix, rows_number):
	cols = len(matrix[0])
	zeros_row = [0 for col in range(cols)]
	for n in range(rows_number):
		matrix.append(zeros_row)
	return matrix

# Complete matrix with zeros until is with n*n format
def make_matrix_square(matrix, desired_size):
	rows = len(matrix)
	cols = len(matrix[0])

	if (rows > desired_size or cols > desired_size):
		raise Exception("Cannot increase matrix size")

	matrix = add_zeros_columns(matrix, desired_size - cols)
	matrix = add_zeros_rows(matrix, desired_size - rows)

	return matrix

##  TESTING
def test_strassen_generalized_multiply(a, b, expected):
	result = strassen_generalized(a, b)
	if (result == expected):
		print("PASSED strassen_generalized - Result:")
		print_matrix(result)
	else:
		print("--> FAILED strassen_generalized - Result:")
		print_matrix(result)
		print("Expected: ")
		print_matrix(expected)
	print()

if __name__ == "__main__":
    main()