from __future__ import division
from time import time
import math
import operator
import functools


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time()
        result = func(*args, **kwargs)
        t1 = time()
        return result, "which took {} s".format(t1-t0)
    return wrapper


# helper
def is_prime(num):
    """Returns True if num is a prime number."""
    return all(num % x for x in xrange(2, num))


def multiples_of_3_and_5(threshold=1000):
    """P1. Find the sum of multiples of 3 or 5 up to a threshold."""
    tot = 0
    for i in xrange(1, threshold):
        if i % 3 == 0 or i % 5 == 0:
            tot += i

    return tot


def even_fibonacci_numbers(threshold=4000000):
    """P2. Finds sum of even valued fibonacci numbers."""
    def make_fib_list(threshold):
        fibs = [1, 2]
        x = sum(fibs)
        i = len(fibs)
        while x <= threshold:
            fibs.append(x)
            # advance to next fib number
            i += 1
            x = fibs[i-2] + fibs[i-1]
        else:
            return fibs

    fibs = make_fib_list(threshold)
    return sum(x for x in fibs if x % 2 == 0)


def largest_prime_factor(n=600851475143):
    """P3. Finds the largest prime factor of n."""
    # def is_prime(num):
    #     return all(num % x for x in xrange(2, num))
    for i in xrange(2, n):
        if n % i == 0:
            # now take its larger factor pair, where i * j = n
            j = int(n / i)
            if is_prime(j):
                return j

    # #for i in xrange(n-1, 1, -1):
    # for i in reversed(xrange(2, n)):
    #     if n % i == 0:
    #         if is_prime(i):
    #             return i
    # else:
    #     return "No prime factors exist!"


def largest_palindrome_product(digits=3):
    """
    P4. Finds the largest palindrome made from the product of two x-digit nums.
    """
    def is_palindrome_int(n):
        """Returns True if an int is a palindrome."""
        s = str(n)
        return s == s[::-1]

    ceil = int('9' * digits)
    floor = int('1' + '0' * (digits-1))
    cutoff = floor
    largest = 0

    for i in xrange(ceil, floor, -1):
        if i < cutoff:
            break
        for j in xrange(ceil, floor, -1):
            if j < cutoff:
                break
            product = i * j
            if is_palindrome_int(product):
                if product > largest:
                    largest = product
                    cutoff = min(i, j)

    return largest


def smallest_multiple(n=20):
    """P5. Finds smallest number evenly divisible by all numbers 1 to n."""
    def get_prime_factors(num):
        """Returns the prime factors for num."""
        pf = []
        for i in xrange(2, num):
            if num % i == 0:
                if is_prime(i):
                    pf.append(i)
        return pf

    def get_necessary_seq(num):
        """Finds the necessary numbers we need to check in a sequence."""
        # NOTE: This turns out to just be the first half of the reversed list
        l = range(num, 0, -1)
        cutoff = int(math.ceil(len(l)/2))
        return l[:cutoff]

    def reduce_to_primes(l):
        """Returns a list of only prime factors from l (dupes allowed)."""
        factors = []
        for i in l:
            pf = get_prime_factors(i)
            if pf:
                factors.extend(pf)
            else:
                factors.append(i)
        return factors

    seq = get_necessary_seq(n)
    primes = reduce_to_primes(seq)
    return reduce(operator.mul, primes)

    # x, start, last_smallest_multiple = 2, 2, 2
    # for i in xrange(start, n+1):
    #     l = find_list_to_check(i)
    #     #x = i
    #     while not is_evenly_divisible(x, l):
    #         x *= i
    #     else:
    #         last_smallest_multiple = x
    #
    # return last_smallest_multiple


if __name__ == '__main__':
    # print multiples_of_3_and_5(1000)
    # print even_fibonacci_numbers(4000000)
    # print largest_prime_factor(9213195)
    # print largest_prime_factor(92130)
    # print largest_palindrome_product(3)
    print smallest_multiple(56)