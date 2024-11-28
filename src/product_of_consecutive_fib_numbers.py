from typing import List

import codewars_test as test

fibonacci_cache: dict[int, int] = {}


def calc_fibonacci(i: int) -> int:
    if i in [0, 1]:
        return i

    if i not in fibonacci_cache:
        fibonacci_cache[i] = calc_fibonacci(i - 1) + calc_fibonacci(i - 2)

    return fibonacci_cache[i]


def product_fib(prod: int) -> List[int | bool]:
    i = 0
    while not calc_fibonacci(i) * calc_fibonacci(i + 1) >= prod:
        i += 1

    return [
        calc_fibonacci(i),
        calc_fibonacci(i + 1),
        calc_fibonacci(i) * calc_fibonacci(i + 1) == prod,
    ]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(product_fib(4895), [55, 89, True])
        test.assert_equals(product_fib(5895), [89, 144, False])
