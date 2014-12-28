from helpers import *


def test_get_pdivisors_0():
    assert get_pdivisors(0) == set()


def test_get_pdivisors_1():
    assert get_pdivisors(1) == set()


def test_get_pdivisors_2():
    assert get_pdivisors(2) == {1}


def test_get_pdivisors_4():
    assert get_pdivisors(4) == {1, 2}


def test_get_pdivisors_11():
    assert get_pdivisors(11) == {1}


def test_get_pdivisors_220():
    assert get_pdivisors(220) == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}


def test_get_pdivisors_284():
    assert get_pdivisors(284) == {1, 2, 4, 71, 142}
