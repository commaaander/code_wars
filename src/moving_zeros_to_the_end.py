from typing import List

import codewars_test as test


def move_zeros(lst: List[int]) -> List[int]:
    non_zeros = [i for i in lst if i != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return [*non_zeros, *zeros]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
