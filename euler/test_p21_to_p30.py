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


def test_get_names_score():
    assert get_name_score('COLIN', 938) == 49714


def test_names_scores():
    assert names_scores() == 871198282


def test_is_abundant_1():
    assert is_abundant(1) is False


def test_is_abundant_8():
    assert is_abundant(8) is False


def test_is_abundant_12():
    assert is_abundant(12) is True


def test_is_abundant_28():
    assert is_abundant(28) is False


def test_non_abundant_sums():
    assert non_abundant_sums() == 4179871


def test_lexicographic_permutations():
    assert lexicographic_permutations() == 2783915604


def test_x_digit_fibonacci_number_3():
    assert x_digit_fibonacci_number(3) == 144


def test_x_digit_fibonacci_number_7():
    assert x_digit_fibonacci_number(7) == 1346269


def test_x_digit_fibonacci_number_1000():
    assert x_digit_fibonacci_number(1000) == 1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816


def test_number_spiral_diagonals_1():
    assert number_spiral_diagonals(1) == 1


def test_number_spiral_diagonals_3():
    assert number_spiral_diagonals(3) == 25


def test_number_spiral_diagonals_5():
    assert number_spiral_diagonals(5) == 101


def test_number_spiral_diagonals():
    assert number_spiral_diagonals() == 669171001
