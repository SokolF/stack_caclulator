from calculator import *
from converter import *
from lexer import *



print('Enter expression')
string = input()

instance = is_valid(string)

if len(instance) == 0:
    print("Incorrect input")
else:
    if "x" in instance:
        print("Enter start of segment")
        x1 = float(input())
        print("Enter end of segment")
        x2 = float(input())
        print("If you want to find the root of the equation: Enter 'Root'\n"
              "If you want to calculate integral: Enter 'Integral'")
        answer = input()
        if answer == "Root":
            print("The root of the equation:", secant_method(Arithmetics(to_postfix(instance)).solve, x1, x2))
        if answer == "Integral":
            print("Integral:", integral(Arithmetics(to_postfix(instance)).solve, x1, x2))

    else:
        if len(to_postfix(instance)) == 0:
            print("Incorrect input")
        else:
            print("Answer:", Arithmetics(to_postfix(instance)).solve(0))