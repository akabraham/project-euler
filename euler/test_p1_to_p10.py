from __future__ import unicode_literals

from conftest import slow
from p1_to_p10 import *


def test_multiples_of_3_and_5():
    assert multiples_of_3_and_5(threshold=10) == 23
    assert multiples_of_3_and_5(threshold=1000) == 233168


def test_even_fibonacci_numbers():
    assert even_fibonacci_numbers(threshold=100) == 44
    assert even_fibonacci_numbers(threshold=4000000) == 4613732


@slow
def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(600851475143) == 6857


def test_largest_palindrome_product():
    assert largest_palindrome_product(digits=2) == 9009
    assert largest_palindrome_product(digits=3) == 906609


def test_smallest_multiple():
    assert smallest_multiple(10) == 2520
    assert smallest_multiple(20) == 6983776800


def test_sum_square_difference():
    assert sum_square_difference(10) == 2640
    assert sum_square_difference(100) == 25164150


@slow
def test_prime_10001st():
    assert prime_10001st(6) == 13
    assert prime_10001st(10001) == 104743


def test_largest_product_in_series():
    assert largest_product_in_series(x=5) == 40824


def test_special_pythagorean_triplet():
    assert special_pythagorean_triplet(1000) == 31875000


@slow
def test_summation_of_primes():
    assert summation_of_primes(10) == 17
    # assert summation_of_primes(2000000) == 142913828922