"""
    Author: Leonardo Ribeiro
    Python Version: 3.8.10
"""

import math

def main():
	run_tests_basic_operations()
	run_multiplication_tests()


def _strassen(a, b):
	"""
	Strassen's Algorithm for matrix multiplication

	Expects two matrices that are n*n with n being a power of two

	For a generalized version (any input) see strassen_generalized.py
	"""

	# Base case - 1x1 matrices being multiplied
	if (len(a[0]) == 1):
		return [[a[0][0]*b[0][0]]]

	[a11, a12, a21, a22] = split(a)
	[b11, b12, b21, b22] = split(b)

	p1 = _strassen(add(a11, a22), add(b11, b22))
	p2 = _strassen(add(a21, a22), b11)
	p3 = _strassen(a11, subtract(b12, b22))
	p4 = _strassen(a22, subtract(b21, b11))
	p5 = _strassen(add(a11, a12), b22)
	p6 = _strassen(subtract(a21, a11), add(b11, b12))
	p7 = _strassen(subtract(a12, a22), add(b21, b22))

	q11 = add(add(p1, p4), subtract(p7, p5))
	q12 = add(p3, p5)
	q21 = add(p2, p4)
	q22 = add(subtract(p1, p2), add(p3, p6))

	return join_quadrants(q11, q12, q21, q22)

def strassen(a, b):
	"""
	Wrapper around Strassen algorithm implementation to validate inputs
	before starting
	"""
	n = len(a[0])
	if (n != len(b)):
		raise Exception("Matrices cannot be multiplied")
	validate_is_power_of_two(n)

	return _strassen(a,b)


# Basic operations

def split(matrix):
	"""
	Splits a n*n (where n is a power of 2) matrix M matrix into quadrants in the form:
	"""
	n = len(matrix)
	n_2 = n // 2

	q11 = zeros_matrix(n_2, n_2)
	q12 = zeros_matrix(n_2, n_2)
	q21 = zeros_matrix(n_2, n_2)
	q22 = zeros_matrix(n_2, n_2)

	for i in range (n_2):
		for j in range (n_2):
			q11[i][j] = matrix[i][j]
			q12[i][j] = matrix[i][j + n_2]
			q21[i][j] = matrix[i + n_2][j]
			q22[i][j] = matrix[i + n_2][j + n_2]

	return [q11, q12, q21, q22]

def join_quadrants(q11, q12, q21, q22):
	"""
	Creates a matrix from it's quadrants
	"""
	n_2 = len(q11)
	n = 2 * n_2
	result = zeros_matrix(n, n)
	for i in range(n):
		for j in range (n):
			if (i < n_2 and j < n_2):
				result[i][j] = q11[i][j]
			elif (i < n_2 and j >= n_2):
				result[i][j] = q12[i][j - n_2]
			elif (i >= n_2 and j < n_2):
				result[i][j] = q21[i - n_2][j]
			elif (i >= n_2 and j >= n_2):
				result[i][j] = q22[i - n_2][j - n_2]
	return result

def add(x, y):
	"""
	Matrices addition -> x + y
	"""
	rows = len(x)
	cols = len(x[0])
	result = zeros_matrix(rows, cols)
	for i in range(rows):
		for j in range(cols):
			result [i][j] = x[i][j] + y[i][j]
	return result

def subtract(x, y):
	"""
	Matrices subtraction -> x - y
	"""
	rows = len(x)
	cols = len(x[0])
	result = zeros_matrix(rows, cols)
	for i in range(rows):
		for j in range(cols):
			result [i][j] = x[i][j] - y[i][j]
	return result


# Helper methods

def zeros_matrix(rows, columns):
	"""
	Initializes a matrix with zeros
	"""
	return [[0 for col in range(rows)] for row in range(columns)]

def validate_is_power_of_two(x):
	"""
	Validates a number is power of two
	"""
	if (not math.log(x, 2).is_integer()):
		raise Exception("Not a power of 2")

def print_matrix(m):
	"""
	Prints a matrix
	"""
	for i in range(len(m)):
		print(m[i])

# Tests for matrix multiplication

def test_strassen_multiply(a, b, expected):
	result = strassen(a, b)
	if (result == expected):
		print("PASSED strassen - Result:")
		print_matrix(result)
	else:
		print("--> FAILED strassen - Result:")
		print_matrix(result)
		print("Expected: ")
		print_matrix(expected)
	print()

def run_multiplication_tests():
	"""
	Runs tests for matrices multiplications with known results
	"""
	test_strassen_multiply(
		[
			[5, 7, 9, 10],
			[2, 3, 3, 8],
			[8, 10, 2, 3],
			[3, 3, 4, 8]
		],
		[
			[3, 10, 12, 18],
			[12, 1, 4, 9],
			[9, 10, 12, 2],
			[3, 12, 4, 10]
		],
		[
			[210, 267, 236, 271],
			[93, 149, 104, 149],
			[171, 146, 172, 268],
			[105, 169, 128, 169]
		]
	)

# Tests for basic operations

def test_split(matrix, expected11, expected12, expected21, expected22):
	quadrants = split(matrix)
	expected_quadrants = [expected11, expected12, expected21, expected22]
	passed = quadrants == expected_quadrants
	if(passed):
		print("PASSED split - Result:")
		for q in quadrants:
			print_matrix(q)
			print()
	else:
		print("--> FAILED split - Result:")
		for q in quadrants:
			print_matrix(q)
			print()
		print("Expected:")
		for q in expected_quadrants:
			print_matrix(q)
			print()
	print()

def test_join_quadrants(q11, q12, q21, q22, expected):
	result = join_quadrants(q11, q12, q21, q22)
	if(result == expected):
		print("PASSED join_quadrants - Result:",)
		print_matrix(result)
	else:
		print("--> FAILED join_quadrants - Result:")
		print_matrix(result)
		print("Expected:")
		print_matrix(expected)
	print()

def test_add(x, y, expected):
	result = add(x, y)
	if(result == expected):
		print("PASSED add - Result:")
		print_matrix(result)
	else:
		print("--> FAILED add - Result:")
		print_matrix(result)
		print("Expected:")
		print_matrix(expected)
	print()

def test_subtract(x, y, expected):
	result = subtract(x, y)
	if(result == expected):
		print("PASSED subtract - Result:")
		print_matrix(result)
	else:
		print("--> FAILED subtract - Result:")
		print_matrix(result)
		print("Expected:")
		print_matrix(expected)
	print()

def run_tests_basic_operations():
	"""
	Runs tests for basic operations known results
	"""
	test_join_quadrants(
		[[1,2],[4,5]],
		[[3,4],[6,7]],
		[[8,9],[11,12]],
		[[10,11],[13,14]],
		[
			[1,2,3,4],
			[4,5,6,7],
			[8,9,10,11],
			[11,12,13,14]
		]
	)
	test_split(
		[
			[1,2,3,4],
			[4,5,6,7],
			[8,9,10,11],
			[11,12,13,14]
		],
		[[1,2],[4,5]],
		[[3,4],[6,7]],
		[[8,9],[11,12]],
		[[10,11],[13,14]]
	)
	test_add([[1,2],[3,4]], [[2,1],[2,1]], [[3,3],[5,5]])
	test_subtract([[1,2],[3,4]], [[2,1],[2,1]], [[-1,1],[1,3]])

# Runs code
if __name__ == "__main__":
    main()