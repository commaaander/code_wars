from solutions.create_phone_number import create_phone_number
from solutions.take_a_ten_minutes_walk import is_valid_walk
from solutions.highest_and_lowest import high_and_low
from solutions.complementary_dna import DNA_strand
from solutions.find_the_next_perfect_square import find_next_square
import _codewars_test as test


def test_create_phone_number():
    test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")


def test_take_a_ten_minutes_walk():
    test.assert_equals(is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]), True, "should return True")
    test.assert_equals(is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]), False, "should return False")
    test.assert_equals(is_valid_walk(["w"]), False, "should return False")
    test.assert_equals(is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]), False, "should return False")


def test_highest_and_lowest():
    test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
    test.assert_equals(high_and_low("1 2 3"), "3 1")


def test_DNA_strand():
    test.assert_equals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
    test.assert_equals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
    test.assert_equals(DNA_strand("GTAT"), "CATA", "String GTAT is")


def test_find_the_next_perfect_square():
    test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
    test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
    test.assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
    test.assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")
    test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
    test.assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")


def test_rgb():
    from solutions.rgb_to_hex_conversion import rgb

    test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
    test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
    test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
    test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
    test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
