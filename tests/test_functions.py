from solutions.create_phone_number import create_phone_number
import codewars_test as test


def test_create_phone_number():
    test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

