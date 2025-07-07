from lib.enums import Operators
from math import pi as PI
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

    def test_invalid_start(self):
        assert parsers.number("a1") == None
        assert parsers.number("apple112213") == None

    def test_invalid_end(self):
        assert parsers.number("123apple") == (123, 3)


class TestOperatorParser:
    def test_exponent(self):
        assert parsers.operator("**") == (Operators.exponent, 2)
        assert parsers.operator("^") == (Operators.exponent, 1)

    def test_multiplication(self):
        assert parsers.operator("*") == (Operators.multiplication, 1)
    
    def test_devision(self):
        assert parsers.operator("/") == (Operators.devision, 1)
    
    def test_addition(self):
        assert parsers.operator("+") == (Operators.addition, 1)
    
    def test_subtraction(self):
        assert parsers.operator("-") == (Operators.subtraction, 1)
    
    def test_invalid_start(self):
        assert parsers.operator("s-") == None

    def test_invalid_end(self):
        assert parsers.operator("-o") == (Operators.subtraction, 1)


class TestConstantParser:
    def test_pi(self):
        assert parsers.constant("pi") == (PI, 2)
