from __future__ import unicode_literals

from time import time
import functools


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time()
        result = func(*args, **kwargs)
        t1 = time()
        return result, "which took {} s".format(t1-t0)
    return wrapper


def is_prime(n):
    """Returns True if n is a prime number."""
    return all(n % i for i in xrange(2, n))