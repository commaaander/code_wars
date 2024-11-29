# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the
# top-3 most occurring words, in descending order of the number of occurrences.
#
# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an
# empty array if a text contains no words.
#
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]
# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]

import logging
import re
from collections import Counter

import codewars_test as test

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def top_3_words(text):
    words = re.findall(r"'*[a-z]+[a-z']*", text.lower())
    word_count = Counter(words)
    most_common_words = word_count.most_common(3)

    return [keys for keys, values in most_common_words]


if __name__ == "__main__":
    test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
    test.assert_equals(top_3_words("  , e   .. "), ["e"])
    test.assert_equals(top_3_words("  ...  "), [])
    test.assert_equals(top_3_words("  '  "), [])
    test.assert_equals(top_3_words("  '''  "), [])
    test.assert_equals(
        top_3_words(
            """In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""
        ),
        ["a", "of", "on"],
    )
