"""
My project euler solutions for p21 to p30.
author: akabraham
"""
from __future__ import unicode_literals, division
from helpers import get_divisors


def is_amicable(a, b):
    """P21 helper. Returns True if x and y are amicable numbers. That is,
    d(a) = b and d(b) = a, where d(n) is the sum of proper divisors of x."""
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


if __name__ == '__main__':
    print amicable_numbers(10000)
    # print names_scores()
