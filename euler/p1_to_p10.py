"""
Project Euler solutions for p1 to p10.
author: akabraham
"""
from __future__ import division, unicode_literals

import math
import operator

from helpers import is_prime, is_prime_check_known, clockit


def multiples_of_3_and_5(threshold=1000):
    """P1. Find the sum of multiples of 3 or 5 up to a threshold."""
    return sum(i for i in range(threshold) if i % 3 == 0 or i % 5 == 0)


def even_fibonacci_numbers(t=4000000):
    """P2. Finds sum of even valued fibonacci numbers."""
    def fib_even(n):
        a, b = 0, 1
        while a < n:
            if a % 2 == 0:
                yield a
            a, b = b, a + b

    return sum(fib_even(t))


def largest_prime_factor(n=600851475143):
    """P3. Finds the largest prime factor of n."""
    for i in xrange(1, n, 2):
        if n % i == 0:
            # use its larger factor pair
            j = n // i
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
        for i in xrange(2, num):
            if num % i == 0 and is_prime(i):
                yield i

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
            pf = list(get_prime_factors(i))
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
    P6. Finds the difference between the sum of squares and the square of the
    sum of the first c numbers.
    """
    def sum_of_squares(x):
        """Computes the sum of the squares for the first x natural numbers."""
        return sum(i**2 for i in xrange(1, x+1))

    def square_of_sum(x):
        """Computes the square of the sum of the first x natural numbers."""
        return sum(range(1, x+1)) ** 2

    return square_of_sum(c) - sum_of_squares(c)


def prime_10001st(x=10001):
    """P7. Finds the xth prime number."""
    i = 3
    primes = [2]
    while len(primes) < x:
        i += 2
        if is_prime_check_known(i, primes):
            primes.append(i)
    else:
        return primes[-1]


def largest_product_in_series(x=5, series=None):
    """P8. Finds the greatest product of x consecutive digits in a series."""
    if not series:
        series = (
            '73167176531330624919225119674426574742355349194934'
            '96983520312774506326239578318016984801869478851843'
            '85861560789112949495459501737958331952853208805511'
            '12540698747158523863050715693290963295227443043557'
            '66896648950445244523161731856403098711121722383113'
            '62229893423380308135336276614282806444486645238749'
            '30358907296290491560440772390713810515859307960866'
            '70172427121883998797908792274921901699720888093776'
            '65727333001053367881220235421809751254540594752243'
            '52584907711670556013604839586446706324415722155397'
            '53697817977846174064955149290862569321978468622482'
            '83972241375657056057490261407972968652414535100474'
            '82166370484403199890008895243450658541227588666881'
            '16427171479924442928230863465674813919123162824586'
            '17866458359124566529476545682848912883142607690042'
            '24219022671055626321111109370544217506941658960408'
            '07198403850962455444362981230987879927244284909188'
            '84580156166097919133875499200524063689912560717606'
            '05886116467109405077541002256983155200055935729725'
            '71636269561882670428252483600823257530420752963450')

    i, largest_prod = 0, 0
    while i < len(series):
        chunk = series[i:i+x]
        prod = reduce(operator.mul, map(int, chunk))
        if prod > largest_prod:
            largest_prod = prod
        i += 1
    else:
        return largest_prod


def special_pythagorean_triplet(val=1000):
    """P9. Finds the product of a Pythagorean triplet where a + b + c = val."""
    for a in xrange(1, val):
        for b in xrange(a + 1, val):
            for c in xrange(b + 1, val):
                if a + b + c == val:
                    if a**2 + b**2 == c**2:
                        # print "Found it! a={} b={} c={}".format(a, b, c)
                        return a * b * c


def summation_of_primes(ceil=2000000):
    """P10. Finds the sum of all primes below ceil."""
    def get_prime_list(c):
        """Returns a list of primes less than ceil."""
        # NOTE: in real life, it would be far more efficient to import a list of
        # primes once you get above ~100,000
        p = [2]
        for i in xrange(3, c, 2):
            if is_prime_check_known(i, p):
                p.append(i)
        return p

    primes = get_prime_list(ceil)
    return sum(primes)


if __name__ == '__main__':
    # print multiples_of_3_and_5(1000)
    # print even_fibonacci_numbers(4000000)
    # print largest_prime_factor()
    # print largest_palindrome_product(3)
    # print smallest_multiple(20)
    # print sum_square_difference(100)
    # print prime_10001st(10001)
    # print largest_product_in_series()
    # print special_pythagorean_triplet()
    print summation_of_primes(2000000)
    pass
