from .enums import Operators
from typing import Any

def get_neighbor(problem: list[Any], direction: int, start: int):
    i = start
    while 0 <= i and i < len(problem):
        i += direction
        result = problem[i]
        if(result):
            return (i, result)

def solve_formula(problem: list[Any], map: dict[str, list[int]]):
    #Brackets
    for pos in map["()"]:
        sub_problem, sub_map = problem[pos]
        problem[pos] = solve_formula(sub_problem, sub_map)

    for operation, task in [
        (Operators.power, lambda a,b: a**b,),
        (Operators.devision, lambda a,b: a/b,),
        (Operators.multiplication, lambda a,b: a*b,),
        (Operators.addition, lambda a,b: a+b,),
        (Operators.subtraction, lambda a,b: a-b)
    ]:
        for pos in map[operation]:
            left = get_neighbor(problem, -1, pos)
            right = get_neighbor(problem, 1, pos)

            problem[left[0]] = task(left[1], right[1])
            problem[pos] = None
            problem[right[0]] = None

    return problem[0]