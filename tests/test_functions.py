from solutions.create_phone_number import create_phone_number
from solutions.take_a_ten_minutes_walk import is_valid_walk
from solutions.highest_and_lowest import high_and_low
from solutions.complementary_dna import DNA_strand
import codewars_test as test


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
