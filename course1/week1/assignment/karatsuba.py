
def karatsuba_multiplication(number1: int, number2: int):
	# Base case
	if (number1 < 10 and number2 < 10):
		return number1 * number2

	n = max(len(str(number1)), len(str(number2)))
	n_2 = n // 2

	a = number1 // pow(10, n_2)
	b = number1 % pow(10, n_2)
	c = number2 // pow(10, n_2)
	d = number2 % pow(10, n_2)

	ac = karatsuba_multiplication(a, c)
	bd = karatsuba_multiplication(b, d)
	ad_bc = karatsuba_multiplication(a + b, c + d)

	ad_plus_bc = ad_bc - ac - bd

	return pow(10, 2*n_2) * ac + pow(10, n_2) * ad_plus_bc + bd

def test(number1, number2):
	result = karatsuba_multiplication(number1, number2)
	expected_result = number1 * number2
	if (result == expected_result):
		print(number1, "*", number2, " = ", result, "OK")
	else:
		print(number1, "*", number2, " ---- FAILED ----")
		print("result: ", result, "expected result: ", expected_result)

test(8568, 2386)
test(2875, 68)
test(2654684185, 32418854854555)
test(484652, 1241579)
test(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)