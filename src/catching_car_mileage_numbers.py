# Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a
# box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending
# on whether it receives a 1 or a 2 (respectively).
#
# It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number
# input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the
# next two miles, or a 0 if the number is not interesting.
#
# Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.
#
# "Interesting" Numbers
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

import logging
import re
from collections import Counter

import codewars_test as test  # type: ignore

logging.basicConfig(level=logging.DEBUG, format="👉 %(message)s")


def is_interesting(number, awesome_phrases) -> int:
    for i in range(3):
        candidate = number + i
        logging.debug(f"Testing {candidate=} / {number=} / {i=}")

        # Number is too small
        if candidate >= 100:
            # Any digit followed by all zeros
            if re.match(r"^[1-9][0]{2,}$", str(candidate)):
                logging.debug(f"Any digit followed by all zeros, return {2 if i == 0 else 1}.")
                return 2 if i == 0 else 1

            # Every digit is the same number
            if len(Counter(str(candidate))) == 0:
                logging.debug(f"Every digit is the same number, return {2 if i == 0 else 1}.")
                return 2 if i == 0 else 1

            # The digits are sequential, incementing
            if is_incrementing(candidate):
                logging.debug(f"The digits are sequential, incementing, return {2 if i == 0 else 1}.")
                return 2 if i == 0 else 1

            # The digits are sequential, decrementing
            if is_decrementing(candidate):
                logging.debug(f"The digits are sequential, decrementing, return {2 if i == 0 else 1}.")
                return 2 if i == 0 else 1

            # The digits are a palindrome
            if str(candidate) == str(candidate)[::-1]:
                logging.debug(f"The digits are a palindrome, return {2 if i == 0 else 1}.")
                return 2 if i == 0 else 1

            # The digits match one of the values in the awesome_phrases array
            if candidate in awesome_phrases:
                logging.debug(
                    f"The digits in match one of the values in {awesome_phrases=}, return {2 if i == 0 else 1}."
                )
                return 2 if i == 0 else 1

    logging.debug(f"Number {number} is not interesting, return 0.")
    return 0


def is_incrementing(number: int) -> bool:
    for i in range(1, len(str(number))):
        n1 = int(str(number)[i - 1])
        n2 = int(str(number)[i])
        if n2 == 0:
            n2 = 10
        if n1 + 1 != n2:
            return False
    return True


def is_decrementing(number: int) -> bool:
    for i in range(1, len(str(number))):
        n1 = int(str(number)[i - 1])
        n2 = int(str(number)[i])
        if n1 - 1 != n2:
            return False
    return True


if __name__ == "__main__":
    tests = [
        {"n": 80083, "interesting": [1337, 256], "expected": 1},
        # {"n": 1336, "interesting": [1337, 256], "expected": 1},
        # {"n": 1337, "interesting": [1337, 256], "expected": 2},
        # {"n": 11208, "interesting": [1337, 256], "expected": 0},
        # {"n": 11209, "interesting": [1337, 256], "expected": 1},
        # {"n": 11211, "interesting": [1337, 256], "expected": 2},
        # {"n": 7540, "interesting": [1337, 256], "expected": 2},
    ]
    for t in tests:
        test.assert_equals(is_interesting(t["n"], t["interesting"]), t["expected"])
        print(33 * "-")
