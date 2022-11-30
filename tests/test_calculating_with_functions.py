import codewars_test as test
from solutions.calculating_with_functions import (
    # one,
    two,
    three,
    four,
    five,
    seven,
    times,
    plus,
    nine,
    eight,
    six,
    divided_by,
    minus,
)


def test_calculating_with_functions():
    test.assert_equals(seven(times(five())), 35)
    test.assert_equals(four(plus(nine())), 13)
    test.assert_equals(eight(minus(three())), 5)
    test.assert_equals(six(divided_by(two())), 3)
