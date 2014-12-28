"""
Project euler solutions for p21 to p30.
author: akabraham
"""
from __future__ import unicode_literals, division
from helpers import get_pdivisors
import itertools


def is_amicable(a, b):
    """P21 helper. Returns True if x and y are amicable numbers. That is,
    d(a) = b and d(b) = a, where d(n) is the sum of proper divisors of x."""
    b_pdivisor_sum = sum(d for d in get_pdivisors(b))
    return b_pdivisor_sum == a and a != b


def amicable_numbers(lim=10000):
    """P21. Finds the sum of amicable numbers under 10000."""
    amicables = set()
    for x in xrange(1, lim + 1):
        y = sum(d for d in get_pdivisors(x))
        if is_amicable(x, y):
            amicables.add(x)
            amicables.add(y)

    return sum(i for i in amicables)


def get_name_score(word, pos):
    """P22 helper. Gets the name score for a word and a position."""
    letters = list(word)
    letter_score = sum(ord(l) - 64 for l in letters)
    return pos * letter_score


def names_scores():
    """P22. Finds the total of all the name scores in the p022_names file."""
    with open('../assets/p022_names.txt', 'r') as f:
        data = f.read()
        names = sorted(d.strip('"') for d in data.split(','))
        return sum(get_name_score(n, names.index(n) + 1) for n in names)


def is_abundant(n):
    """P23 helper. Returns whether n is abundant (i.e. the sum of proper
    divisors is greater than n)."""
    pdivisor_sum = sum(d for d in get_pdivisors(n))
    return pdivisor_sum > n


def non_abundant_sums():
    """P23. Finds the sum of all positive integers which can't be written as
    the sum of two abundant numbers. Note all numbers > 28123 can be
    written as the sum of two abundants."""
    abundants = [i for i in xrange(1, 28124) if is_abundant(i)]
    abundant_summables = set(
        sum(c) for c in itertools.combinations_with_replacement(abundants, 2))
    non_abundant_summables = set(xrange(1, 28124)) - abundant_summables
    return sum(x for x in non_abundant_summables)


def lexicographic_permutations(n=1000000):
    """P24. Finds the nth lexicographic permutation of the digits 0 - 9"""
    perm_tuple = list(itertools.permutations(xrange(10)))[n]
    return int(''.join(str(e) for e in perm_tuple))


def x_digit_fibonacci_number(x=1000):
    """P25. Finds the first term in the Fibonacci sequence to contain x
    digits."""
    a, b = 0, 1
    while x > len(str(b)):
        a, b = b, a + b
    else:
        return b


# def reciprocal_cycles(x=1000):
#     """P26. Finds the value of d < x for which 1/d contains the longest
#     recurring cycle in its decimal fraction part."""
#
#
# def quadratic_primes():
#     """P27. """
#
#
# def number_spiral_diagonals():
#     """P28. """
#     # up-right: y = (2x + 1)**2
#     # down-left: y = 2x**2 + 1
#     # down-right: y = 2x**2 - 2x + 1
#     # up-left: y = 2x**2 + 2x + 1


if __name__ == '__main__':
    # print amicable_numbers(10000)
    # print names_scores()
    # print non_abundant_sums()
    # print lexicographic_permutations()
    # print list(get_fibs(7))
    print x_digit_fibonacci_number()
