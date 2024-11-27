import codewars_test as test


def spin_words(sentence: str) -> str:
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split(" "))


@test.describe("Stop gninnipS My sdroW!")
def fixed_tests():
    @test.it("Single word")
    def _():
        test.assert_equals(spin_words("Welcome"), "emocleW")
        test.assert_equals(spin_words("to"), "to")
        test.assert_equals(spin_words("CodeWars"), "sraWedoC")

    @test.it("Multiple words")
    def _():
        test.assert_equals(
            spin_words("Hey fellow warriors"),
            "Hey wollef sroirraw",
        )
        test.assert_equals(
            spin_words("This sentence is a sentence"),
            "This ecnetnes is a ecnetnes",
        )
