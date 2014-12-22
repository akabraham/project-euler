from __future__ import unicode_literals

from p21_to_p30 import *


def test_is_amicable_220_284():
    assert is_amicable(220, 284) is True


def test_is_amicable_221_285():
    assert is_amicable(221, 285) is False


def test_amicable_numbers_1():
    assert amicable_numbers(1) == 0


def test_amicable_numbers():
    assert amicable_numbers(10000) == 31626
