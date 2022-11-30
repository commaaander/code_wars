import _codewars_test as test

from solutions.rgb_to_hex_conversion import rgb


def test_fixed_tests():
    test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
    test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
    test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
    test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
    test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


if __name__ == "__main__":
    test_fixed_tests()
