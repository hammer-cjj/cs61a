def tree(root_label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root_label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def print_tree(t, indent = 0):
	print(' ' * indent + str(label(t)))
	for b in branches(t):
		print_tree(b, indent + 1)

# Problem 1.1
def height(t):
	"""Return the height of a tree.
	>>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
	>>> height(t)
	2
	"""
	if is_leaf(t):
		return 0
	else:
		return max([1 + height(b) for b in branches(t)])

# Problem 1.2
def square_tree(t):
	"""Return a tree with the square of every element in t
	>>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]),tree(8)])])
	>>> print_tree(square_tree(numbers))
	1
	 4
	  9
	  16
	 25
	  36
	   49
	  64
	"""
	bs = [square_tree(b) for b in branches(t)]
	return tree(label(t) * label(t), bs)

# Problem 1.3
def find_path(tree, x):
	"""
	>>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
	>>> find_path(t, 5)
	[2, 7, 6, 5]
	>>> find_path(t, 10) # returns None
	"""
	if label(tree) == x:
		return [label(tree)]
	for b in branches(tree):
		path = find_path(b, x)
		if path:
			return [label(tree)] + path

# Problem 2.2
def add_this_many(x, el, lst):
	"""Adds el to the end of lst the number of times x occurs
	in lst.
	>>> lst = [1,2,4,2,1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2,2,lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	count = 0
	for e in lst:
		if e == x:
			count += 1
	while count > 0:
		lst.append(el)
		count -= 1

# Problem 2.3
def group_by(s, fn):
	"""
	>>> group_by([12, 23, 14, 45], lambda p: p // 10) 
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x * x)
	{9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
	"""
	ret = {}
	for _ in s:
		if fn(_) in ret:
			ret[fn(_)].append(_)
		else:
			ret[fn(_)] = [_]
	return ret

def partition_options(total, biggest): 
	"""
	>>> partition_options(2, 2)
	[[2], [1, 1]]
	>>> partition_options(3, 3)
	[[3], [2, 1], [1, 1, 1]]
	>>> partition_options(4, 3)
	[[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
	"""
	if total == 0:
		return [[]]
	elif total < 0 or biggest == 0:
		return []
	else:
		with_biggest = partition_options(total - biggest, biggest)
		without_biggest = partition_options(total, biggest - 1)
		with_biggest = [[biggest] + elem for elem in with_biggest]

		return with_biggest + without_biggest





























	


























