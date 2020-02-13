# Question 1.1
def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if m == 1:
		return n
	else:
		return multiply(m - 1, n) + n

# Question 1.2
def rec(x, y):
	if y > 0:
		return x * rec(x, y - 1)
	return 1

# Question 1.3
def hailstone(n):
	"""Print out the hailstone sequence starting at n, and return the
	number of elements in the sequence.

	>>> a = hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>> a
	7
	"""
	print(n)
	if n == 1:
		return 1
	elif n % 2 == 0:
		n = n // 2
		return 1 + hailstone(n)
	elif n % 2 != 0:
		n = n * 3 + 1
		return 1 + hailstone(n)

# Question 1.4 
def is_prime(n):
	"""
	>>> is_prime(7)
	True
	>>> is_prime(10)
	False
	>>> is_prime(1)
	False
	"""
	def prime_helper(k):
		if k == 1:
			return 1
		elif n % k == 0:
			return 1+prime_helper(k - 1)
		else:
			return prime_helper(k - 1)

	return prime_helper(n) == 2

# Question 1.5
def merge(n1, n2):
	"""Merges two numbers
	>>> merge(31, 42)
	4321
	>>> merge(21, 0)
	21
	>>> merge(21, 31)
	3211
	"""
	if n1 == 0:
		return n2
	if n2 == 0:
		return n1
	else:
		n1_rightmost = n1 % 10
		n2_rightmost = n2 % 10
		if n1_rightmost > n2_rightmost:
			return merge(n1, n2 // 10) * 10 + n2_rightmost
		elif n2_rightmost > n1_rightmost:
			return merge(n1 // 10, n2) * 10 + n1_rightmost
		else:
			return merge(n1 // 10, n2 // 10) * 100 + n1_rightmost * 10 + n2_rightmost

# Question 1.6(Optional)
def make_func_repeater(f, x):
	"""
	>>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
	>>> incr_1(2) #same as f(f(x))
	3
	>>> incr_1(5)
	6
	"""
	def repeat(y):
		if y == 0:
			return x
		else:
			return make_func_repeater(f, f(x))(y - 1)
	return repeat






















