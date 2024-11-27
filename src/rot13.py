import re

import codewars_test as test  # type: ignore


def rot13(message: str) -> str:
    ret_val = ""
    for letter in message:
        if re.match(r"[a-z]", letter):
            ascii_value = ord(letter) + 13
            if ascii_value > ord("z"):
                ascii_value -= 26
            letter = chr(ascii_value)
        if re.match(r"[A-Z]", letter):
            ascii_value = ord(letter) + 13
            if ascii_value > ord("Z"):
                ascii_value -= 26
            letter = chr(ascii_value)
        ret_val += letter
    return ret_val


@test.describe("Fixed tests")
def tests():
    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(rot13("test"), "grfg", "Returned solution incorrect for fixed string = test")
        test.assert_equals(rot13("Test"), "Grfg", "Returned solution incorrect for fixed string = Test")
        test.assert_equals(
            rot13("aA bB zZ 1234 *!?%"),
            "nN oO mM 1234 *!?%",
            "Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%",
        )
