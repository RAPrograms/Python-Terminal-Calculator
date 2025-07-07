from lib.solver import solve_formula
from lib.parsers import parse
import sys

def get_inputted_equation():
    result = "".join(sys.argv[1:])
    if(result == ""):
        result = input("What's the problem?\n")
    
    return result

def solve(equation):
    problem, _, map = parse(equation)
    print(solve_formula(problem, map))

if __name__ == "__main__":
    
    solve("((42-1*2)/(9.8+20%))*0.25") #1
    solve("(2**2)^0.5") #2
    solve("1") #1
    #solve("0-1") #CANNOT HANDLE NEGATIVE NUMBERS
    #solve(get_inputted_equation())