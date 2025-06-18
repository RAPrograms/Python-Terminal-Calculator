from lib.solver import solve_formula
from lib.parsers import parse
import sys

def get_inputted_equation():
    result = "".join(sys.argv[1:])
    if(result == ""):
        result = input("What's the problem?\n")
    
    return result


if __name__ == "__main__":
    equation = get_inputted_equation()
    problem, _, map = parse(equation)
    print(solve_formula(problem, map))