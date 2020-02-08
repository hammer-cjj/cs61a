# question 2.3

def count_digits(n):
	'''
		>>> count_digits(4)
		1
		>>> count_digits(12345678)
		8
		>>> count_digits(0)
		0
	'''
	count = 0;
	while n > 0:
		count += 1
		n = n // 10
	return count

# question 2.4

def count_matches(n, m):
	'''
	>>> count_matches(10, 30)
	1
	>>> count_matches(12345, 23456)
	0
	>>> count_matches(121212, 123123)
	2
	>>> count_matches(111, 11) # only one's place natches
	2
	>>> count_matches(101, 10) # no place matches
	0
	'''
	count = 0
	while n > 0 and m > 0:
		if n % 10 == m % 10:
			count += 1
		n, m = n // 10, m // 10
	return count

# question 4.5

def make_skipper(n):
	"""
	>>> a = make_skipper(2)
	>>> a(5)
	1
	3
	5
	"""
	def f(x):
		k = 0
		while k <= x:
			if not k % n == 0:
				print(k)
			k = k + 1
	return f

# question 5.1


def ordered_digits(x):
	"""
	>>> ordered_digits(5)
	True
	>>> ordered_digits(11)
	True
	>>> ordered_digits(127)
	True
	>>> ordered_digits(1357)
	True
	>>> ordered_digits(21)
	False
	>>> result = ordered_digits(1375) # Return, don't print
	>>> result
	False
	"""
	t,x = x % 10, x // 10
	while x > 0:
		if x % 10 > t:
			return False
		t, x = x % 10, x // 10
	return True

# question 5.1

def add1(x):
	return x + 1

def times2(x):
	return x * 2

def add3(x):
	return x + 3

def cycle(f1, f2, f3):
	"""Return a function that is itself  a higher-order function.

	>>> my_cycle = cycle(add1, times2, add3)
	>>> identity = my_cycle(0)
	>>> identity(5)
	5
	>>> add_one_then_double = my_cycle(2)
	>>> add_one_then_double(1)
	4
	>>> do_all_functions = my_cycle(3)
	>>> do_all_functions(2)
	9
	>>> do_more_than_a_cycle = my_cycle(4)
	>>> do_more_than_a_cycle(2)
	10
	>>> do_two_cycles = my_cycle(6)
	>>> do_two_cycles(1)
	19
	"""
	def f(n):
		def g(x):
			k = 1
			v = x
			while k <= n:
				if k % 3 == 1:
					v = f1(v)
				elif k % 3 == 2:
					v = f2(v)
				else:
					v = f3(v)
				k += 1
			return v
		return g
	return f

# question 5.3

def is_palindrome(n):
	"""
	>>> is_palindrome(12321)
	True
	>>> is_palindrome(42)
	False
	>>> is_palindrome(2015)
	False
	>>> is_palindrome(55)
	True
	"""
	x, y = n, 0
	f = lambda : y * 10 + x % 10 
	while x > 0:
		x, y = x // 10 ,f()
	return y == n


































