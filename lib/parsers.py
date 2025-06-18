from .enums import Operators
from typing import Any

def number(equation: str, start: int = 0) -> tuple[float, int] | None:
    buffer = ""
    percentage = False

    for i in range(start, len(equation)):
        char = equation[i]
        if(char == "%"):
            percentage = True
            break

        if(char not in "0123456789."):
            break

        buffer += char

    if(buffer == ""):
        return None

    length = len(buffer)
    numb = float(buffer)
    if(percentage):
        numb /= 100
        length += 1

    return (numb, length)


def parse_operator(equation: str, start: int = 0) -> tuple[list[Any], int]:
    match(equation[start]):
        case "^":
            return (Operators.power, 1)

        case "+":
            return (Operators.addition, 1)

        case "-":
            return (Operators.subtraction, 1)

        case "/":
            return (Operators.devision, 1)

        case "*":
            if(equation[start:start+2] == "**"):
                return (Operators.power, 2)
            return (Operators.multiplication, 1)
       
        case _:
            return None