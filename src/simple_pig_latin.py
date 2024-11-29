import logging
import string

import codewars_test as test  # type: ignore

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def pig_it(text: str) -> str:
    pig_text: str = ""
    for word in text.split():
        if word in string.punctuation:
            pig_text += word
        else:
            pig_text += word[1:] + word[0] + "ay "

    return pig_text.strip()


if __name__ == "__main__":
    test.assert_equals(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
    test.assert_equals(pig_it("This is my string !"), "hisTay siay ymay tringsay !")
