from helpers import *


def test_get_divisors_0():
    assert get_divisors(0) == set()


def test_get_divisors_1():
    assert get_divisors(1) == set()


def test_get_divisors_2():
    assert get_divisors(2) == {1}


def test_get_divisors_4():
    assert get_divisors(4) == {1, 2}


def test_get_divisors_11():
    assert get_divisors(11) == {1}


def test_get_divisors_220():
    assert get_divisors(220) == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}


def test_get_divisors_284():
    assert get_divisors(284) == {1, 2, 4, 71, 142}
