"""
    Author: Leonardo Ribeiro
    Python Version: 3.8.10

	Solving the problem of finding the closest pair of points in a plane

	Running time:
	Brute force - O(n^2)
	Recursively (including pre-sorting operation) - O(n*log(n))
"""
from typing import List, Tuple
import random

# Type definitions
Point = Tuple[float, float] # Example: (1, 2). Where x = 1, y = 2
PairAndDistance = Tuple[List[Point], float] # Example: ([(1,1),(1,2)], 1)

def main():
	run_tests()

def find_closest_pair(points: List[Point]):
	"""
	Sorts the list by x and y coordinates before calling the actual recursive method

	Since sorting can be done in O(n*log(n)), the overall running time is still O(n*log(n))
	"""
	points_sorted_by_x = sorted(points, key=lambda point: point[0])
	points_sorted_by_y = sorted(points, key=lambda point: point[1])
	return _find_closest_pair(points_sorted_by_x, points_sorted_by_y)

def _find_closest_pair(points_sorted_by_x: List[Point], points_sorted_by_y: List[Point]) -> PairAndDistance:
	"""
	Recursive implementation of find_closest pair

	Running time: O(n*log(n))
	"""
	n = len(points_sorted_by_x)
	n_2 = n // 2

	# Base case
	if (n < 4):
		return brute_force_closest_pair(points_sorted_by_x)

	# Splits the lists in half (x coordinate)
	left_by_x = points_sorted_by_x[ : n_2]
	right_by_x = points_sorted_by_x[n_2 : ]

	# Creates left and right lists sorted by y coordinate
	x_middle = left_by_x[n_2 - 1][0]
	left_by_y = []
	right_by_y = []
	for point in points_sorted_by_y:
		if (point[0] <= x_middle):
			left_by_y.append(point)
		else:
			right_by_y.append(point)

	# Recursevely finds closest pair and distance on both sides
	(pair_left, delta_left) = _find_closest_pair(left_by_x, left_by_y)
	(pair_right, delta_right) = _find_closest_pair(right_by_x, right_by_y)

	# Infers closest pair and minimum delta between points halves
	if (delta_left < delta_right):
		delta = delta_left
		closest_pair = pair_left
	else:
		delta = delta_right
		closest_pair = pair_right

	# Builds a list of the points where (x_middle - delta) < x < (x_middle + delta)
	# The result is ordered by y coordinates (since we use the pre-ordered list)
	middle_strip = []
	for point in points_sorted_by_y:
		if (abs(x_middle - point[0]) < delta):
			middle_strip.append(point)

	# Finds potential split pairs (one point on the left and other on the right)
	# where distance is less than delta
	for i in range(len(middle_strip)):
		# Inner loop runs at most 7 times. So it's O(1)
		for j in range(i + 1, min(i + 8, len(middle_strip))):
			if (calculate_distance(middle_strip[i], middle_strip[j]) < delta):
				closest_pair = [middle_strip[i], middle_strip[j]]
				delta = calculate_distance(middle_strip[i], middle_strip[j])

	return (closest_pair, calculate_distance(closest_pair[0], closest_pair[1]))

def brute_force_closest_pair(points: List[Point]) -> PairAndDistance:
	"""
	Brute force implementation to find closest pair
	Returns a tuple contaning the pair of points and the distance

	Running time: O(n^2)
	"""
	n = len(points)

	# Initializing
	min_distance = calculate_distance(points[0], points[1])
	closest_pair = [points[0], points[1]]

	for i in range(0, n):
		for j in range(i + 1, n):
			distance = calculate_distance(points[i], points[j])
			if	(distance < min_distance):
				min_distance = distance
				closest_pair = [points[i], points[j]]

	return (closest_pair, min_distance)

def calculate_distance(p1: Point, p2: Point) -> float:
	"""
	Calculate the distance between two points
	"""
	dx = (p1[0] - p2[0])
	dy = (p1[1] - p2[1])
	return (dx**2 + dy**2)**(1 / 2)

def run_tests():
	"""
	Tests the algorithm for 200 randomly generated lists of points (x, y)
	with random number of elements (from 2 to 500)

	Important observation:
	Note that the distance returned must be equal to the brute force solution,
	but the pairs of points are not necessarily equal.

	That is because when there is a tie (in distance) between pairs,
	both solutions returns only one of the pairs and there is no tiebreaker defined.
	"""
	print("Running tests...")
	passed = True
	for test_count in range(200):
		list = [divmod(ele, 50 + 1) for ele in random.sample(range((50 + 1) * (50 + 1)), random.randint(2, 500))]
		(pair_from_brute_force, distance_from_brute_force) = brute_force_closest_pair(list)
		(pair_from_recursion, distance_from_recursion) = find_closest_pair(list)
		if (not (distance_from_recursion == distance_from_brute_force)):
			passed = False
			break
	if (passed):
		print("PASSED")
	else:
		print("FAILED in test number", test_count + 1, "with input:")
		print(list)
		print("brute_force_result: ", pair_from_brute_force," - Distance: ", distance_from_brute_force)
		print("recursive_result: ", pair_from_recursion," - Distance: ", distance_from_recursion)
	print()

main()
