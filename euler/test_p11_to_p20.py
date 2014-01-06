from __future__ import unicode_literals

from conftest import slow
from p11_to_p20 import *


def test_largest_product_in_grid():
    assert largest_product_in_grid(c=4) == 70600674


def test_highly_divisible_triangular_number():
    assert highly_divisible_triangular_number(divisors=5) == 28
    assert highly_divisible_triangular_number(divisors=500) == 76576500


def test_large_sum():
    assert large_sum(digits=10) == 5537376230


@slow
def test_longest_collatz_sequence():
    # assert longest_collatz_sequence(ceil=1000000) == 837799
    pass


def test_lattice_paths():
    assert lattice_paths(2) == 6
    assert lattice_paths(20) == 137846528820


def test_power_digit_sum():
    assert power_digit_sum(x=15) == 26
    assert power_digit_sum(x=1000) == 1366


def test_number_letter_counts():
    assert number_letter_counts(5) == 19
    assert number_letter_counts(1000) == 21120