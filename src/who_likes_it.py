from os import name
from typing import List

import codewars_test as test


def likes(names: List[str]) -> str:
    match names:
        case []:
            return "no one likes this"
        case [a]:
            return f"{a} likes this"
        case [a, b]:
            return f"{a} and {b} like this"
        case [a, b, c]:
            return f"{a}, {b} and {c} like this"
        case [a, b, *others]:
            return f"{a}, {b} and {len(others)} others like this"
    return ""


@test.it("Basic tests")
def _():
    test.assert_equals(likes([]), "no one likes this")
    test.assert_equals(likes(["Peter"]), "Peter likes this")
    test.assert_equals(likes(["Jacob", "Alex"]), "Jacob and Alex like this")
    test.assert_equals(likes(["Max", "John", "Mark"]), "Max, John and Mark like this")
    test.assert_equals(likes(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")
