
from math import pi as PI
from typing import Any

def number(equation: str, start: int = 0) -> tuple[float, int] | None:
    buffer = ""
    percentage = False

    for char in equation[start:]:
        if(char == "%"):
            percentage = True
            break

        if(char not in "0123456789."):
            break

        buffer += char
    
    if(buffer == ""):
        return None

    numb = float(buffer)
    if(percentage):
        numb /= 100
    length = len(buffer)

    return (numb, length)


def operator(equation: str, start: int = 0) -> tuple[str, int]:
    if equation[start] in ["^","+","-","/"]:
        return (equation[start],1)
    
    elif equation[start] == "*":
        if(equation[start:start+2] == "**"):
            return ("^", 2)
        return ("*", 1)
    
    else:
        return None
        
def constant(equation: str, start: int = 0) -> tuple[Any, int]:
    if(equation[start:start+2].lower() == "pi"):
        return (PI, 2)


def parse(equation: str, start: int = 0) -> tuple[list[Any], int, dict[str, list[int]]]:
    assert start < len(equation), "Invalid Starting Index"
    output = []
    map = {
        "+": [],
        "-": [],
        "/": [],
        "*": [],
        "^": [],
        "()": []
    }

    i = start
    while i < len(equation):
        char = equation[i]
        if(char == ")"):
            return (output, i - start, map)

        if(char == "("):
            data, length, sub_map = parse(equation, i+1)
            i+= length + 2
            output.append((data, sub_map))
            map["()"].append(len(output) - 1)
            continue


        numb_results = number(equation, i)
        if(numb_results):
            i += numb_results[1]
            output.append(numb_results[0])
            if(numb_results[0] < 0):
                map["-"].append(len(output))
            continue


        operator_results = operator(equation, i)
        if(operator_results):
            i += operator_results[1]
            map[operator_results[0]].append(len(output))
            output.append(operator_results[0])
            continue


        constant_results = constant(equation, i)
        if(constant_results):
            i += constant_results[1]
            output.append(constant_results[0])
            continue

        i+= 1

    return (output, i - start, map)