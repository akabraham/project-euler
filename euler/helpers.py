from __future__ import unicode_literals

from time import time
import functools


def clockit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time()
        result = func(*args, **kwargs)
        t1 = time()
        return result, "This took {} s".format(t1-t0)
    return wrapper


# def is_prime(n):
#     """Returns True if n is a prime number."""
#     return all(n % i for i in xrange(2, n))


def is_prime(n):
    """Returns True if n is a prime number."""
    for i in xrange(2, n):
        if n % i == 0:
            return False
    else:
        return True


def is_prime_check_known(n, known_primes):
    """Returns True if n is a prime. Checks only in provided seq."""
    for j in known_primes:
        if n % j == 0:
            return False
    else:
        return True