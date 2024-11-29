#!/usr/bin/env python

import re

import codewars_test as test


def domain_name(url: str) -> str:
    match = re.search(r"(http[s]*://)?(www\.)?(.*?)(\..*)", url)
    if match and match.group(3):
        return match.group(3)
    else:
        return ""


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(domain_name("http://google.com"), "google")
        test.assert_equals(domain_name("http://google.co.jp"), "google")
        test.assert_equals(domain_name("https://123.net"), "123")
        test.assert_equals(domain_name("https://hyphen-site.org"), "hyphen-site")
        test.assert_equals(domain_name("http://codewars.com"), "codewars")
        test.assert_equals(domain_name("www.xakep.ru"), "xakep")
        test.assert_equals(domain_name("https://youtube.com"), "youtube")
        test.assert_equals(domain_name("http://www.codewars.com/kata/"), "codewars")
        test.assert_equals(domain_name("icann.org"), "icann")
