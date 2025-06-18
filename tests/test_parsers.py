from lib import parsers

class TestNumberParser:
    def test_small_number(self):
        assert parsers.number("1") == (1, 1)

    def test_big_number(self):
        assert parsers.number("100") == (100, 3)

    def test_decimal_number(self):
        assert parsers.number("1.50") == (1.5, 4)

    def test_percentage_number(self):
        assert parsers.number("20%") == (0.2, 3)

    def test_non_starting_number(self):
        assert parsers.number("a1") == None
        assert parsers.number("apple112213") == None

    def test_number_cut(self):
        assert parsers.number("123apple") == (123, 3)