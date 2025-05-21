#1)1. Create & import your own module
def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero"
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python math_utils.py <num1> <num2> <operation>")
        print("Operations: add, subtraction, multiplication, division")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        op = sys.argv[3].lower()

        operations = {
            "add": add,
            "subtraction": subtraction,
            "multiplication": multiplication,
            "division": division
        }

        if op in operations:
            result = operations[op](num1, num2)
            print("Result:", result)
        else:
            print(f"Unknown operation '{op}'. Use: add, subtraction, multiplication, division")
    except ValueError:
        print("Please provide valid numbers.")
