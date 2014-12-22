"""
My project euler solutions for p21 to p30.
author: akabraham
"""
from __future__ import unicode_literals, division
from helpers import get_divisors


def is_amicable(a, b):
    """Returns True if x and y are amicable numbers. That is, d(a) = b and
    d(b) = a, where d(n) is the sum of proper divisors of x."""
    b_divisor_sum = sum(d for d in get_divisors(b))
    return b_divisor_sum == a and a != b


def amicable_numbers(lim=10000):
    """P21. Finds the sum of amicable numbers under 10000."""
    amicables = set()
    for x in xrange(1, lim + 1):
        y = sum(d for d in get_divisors(x))
        if is_amicable(x, y):
            amicables.add(x)
            amicables.add(y)

    return sum(i for i in amicables)


if __name__ == '__main__':
    print amicable_numbers(10000)
