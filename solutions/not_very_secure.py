# In this example you have to validate if a user input string is alphanumeric. The given string is not
# nil/null/NULL/None, so you don't have to check that.
# The string has the following conditions to be alphanumeric:
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

import logging
import re

import codewars_test as test

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def alphanumeric(password):
    try:
        is_secure = re.findall(r"[a-zA-Z0-9]+", password)[0] == password
    except Exception:
        is_secure = False

    return is_secure


if __name__ == "__main__":
    test.assert_equals(alphanumeric("hello world_"), False)
    test.assert_equals(alphanumeric("PassW0rd"), True)
    test.assert_equals(alphanumeric("     "), False)
