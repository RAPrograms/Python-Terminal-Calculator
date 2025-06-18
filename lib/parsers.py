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


def operator(equation: str, start: int = 0) -> tuple[list[Any], int]:
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
        


def parse(equation: str, start: int = 0) -> tuple[list[Any], int, dict[str, list[int]]]:
    assert start < len(equation), "Invalid Starting Index"
    output = []
    map = {
        Operators.addition: [],
        Operators.subtraction: [],
        Operators.devision: [],
        Operators.multiplication: [],
        Operators.power: [],
        "()": []
    }

    i = start
    while i < len(equation):
        char = equation[i]
        if(char == ")"):
            return (output, i - start, map)

        if(char == "("):
            data, length, sub_map = parse(equation, i+1)
            i+= length + 1
            output.append((data, sub_map))
            map["()"].append(len(output) - 1)
            continue


        numb_results = number(equation, i)
        if(numb_results):
            i += numb_results[1]
            output.append(numb_results[0])
            if(numb_results[0] < 0):
                map[Operators.subtraction].append(len(output))
            continue


        operator_results = operator(equation, i)
        if(operator_results):
            i += operator_results[1]
            map[operator_results[0]].append(len(output))
            output.append(operator_results[0])
            continue

        i+= 1

    return (output, i - start, map)

