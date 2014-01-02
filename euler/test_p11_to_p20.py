from p11_to_p20 import *


def test_largest_product_in_grid():
    assert largest_product_in_grid(c=4) == 70600674


def test_highly_divisible_triangular_number():
    assert highly_divisible_triangular_number(divisors=5) == 28
    assert highly_divisible_triangular_number(divisors=500) == 76576500


def test_large_sum():
    assert large_sum(digits=10) == 5537376230