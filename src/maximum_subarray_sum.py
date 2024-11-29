from typing import List

import codewars_test as test


def max_sequence(arr: List[int]) -> int:
    max_sum: int = 0
    current_sum: int = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


@test.describe("Fixed tests")
def tests():
    @test.it("Should work on an empty array")
    def test_empty_array():
        test.assert_equals(max_sequence([]), 0)

    @test.it("Should obtain correct maximum subarray sum in the array from the kata description example")
    def test_example_array():
        test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    @test.it("Should obtain correct maximum subarray sum in an example with negative numbers")
    def test_negative_array():
        test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    @test.it("Should obtain correct maximum subarray sum in a complex example")
    def test_complex_array():
        test.assert_equals(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)
