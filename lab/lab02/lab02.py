"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    """
    def h(x):
        def f(y):
            return func(x, y)
        return f
    return h
    """
    return lambda x: lambda y: func(x, y)

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def h(N):
        count, k = 0, 1
        while k<= N:
            if condition(N, k):
                count += 1
            k += 1
        return count
    return h


def both_paths(sofar="S"):
    """
    >>> left, right = both_paths()
    S
    >>> leftleft, leftright = left()
    SL
    >>> rightleft, rightright = right()
    SR
    >>> _ = leftleft()
    SLL
    """
    print(sofar)
    def left_h(s1):
        def left():
            s = s1 + "L"
            print(s)
            return left_h(s), right_h(s)
        return left
    def right_h(s2):
        def right():
            s = s2 + "R"
            print(s)
            return left_h(s), right_h(s)
        return right
    return left_h(sofar), right_h(sofar)

