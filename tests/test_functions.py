from solutions.create_phone_number import create_phone_number
from solutions.take_a_ten_minutes_walk import is_valid_walk
import codewars_test as test


def test_create_phone_number():
    test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")


def test_take_a_ten_minutes_walk():
    test.assert_equals(is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]), True, "should return True")
    test.assert_equals(is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]), False, "should return False")
    test.assert_equals(is_valid_walk(["w"]), False, "should return False")
    test.assert_equals(is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]), False, "should return False")


