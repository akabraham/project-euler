from __future__ import division, unicode_literals

import math
import operator

from helpers import is_prime


def multiples_of_3_and_5(threshold=1000):
    """P1. Find the sum of multiples of 3 or 5 up to a threshold."""
    return sum(i for i in xrange(1, threshold) if i % 3 == 0 or i % 5 == 0)


def even_fibonacci_numbers(threshold=4000000):
    """P2. Finds sum of even valued fibonacci numbers."""
    def make_fib_list(thresh):
        fibs = [1, 2]
        x = sum(fibs)
        i = len(fibs)
        while x <= thresh:
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
    # TODO: investigate if this can be calculated quicker
    for i in xrange(2, n):
        if n % i == 0:
            # now take its larger factor pair, where i * j = n
            j = int(n / i)
            if is_prime(j):
                return j


def largest_palindrome_product(digits=3):
    """
    P4. Finds the largest palindrome made from product of two x-digit nums.
    """
    def is_palindrome_int(n):
        """Returns True if n (an int) is a palindrome."""
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
        cutoff = math.ceil(len(l)/2)
        return l[:int(cutoff)]

    def reduce_to_primes(l):
        """Returns a list of only prime factors from l (yes dupes allowed)."""
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


def sum_square_difference(c=100):
    """
    P6. Finds the difference between the sum of squares the first c numbers and
    the square of the sum.
    """
    def sum_of_squares(x):
        """Computes the sum of the squares for the first x natural numbers."""
        squares = []
        [squares.append(i**2) for i in xrange(1, x+1)]
        return sum(e for e in squares)

    def square_of_sum(x):
        """Computes the square of the sum of the first x natural numbers."""
        sums = sum(i for i in xrange(1, x+1))
        return sums**2

    sum_part = sum_of_squares(c)
    square_part = square_of_sum(c)
    return square_part - sum_part


if __name__ == '__main__':
    # print multiples_of_3_and_5(1000)
    # print even_fibonacci_numbers(4000000)
    # print largest_prime_factor()
    # print largest_palindrome_product(3)
    # print smallest_multiple(20)
    print sum_square_difference(100)
    pass