# algebra_generator.py — Algebra Problem Generator
# Author: LaxmiPrasad Konduri
# Description: Generates random algebra problems for practice.

import random

def generate_linear():
    """Generates a linear equation in the form ax + b = c"""
    a = random.randint(1, 10)
    b = random.randint(0, 20)
    x = random.randint(0, 20)
    c = a * x + b
    print(f"Solve for x: {a}x + {b} = {c}")
    user_answer = float(input("Your answer: "))
    if user_answer == x:
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is {x}\n")

def generate_quadratic():
    """Generates a simple quadratic equation: x^2 + bx + c = 0"""
    # Only generate easy integer solutions
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    # Equation: (x - x1)(x - x2) = 0 => x^2 - (x1+x2)x + x1*x2 = 0
    b = -(x1 + x2)
    c = x1 * x2
    print(f"Solve for x: x^2 + ({b})x + ({c}) = 0")
    user_answers = input("Enter both solutions separated by comma: ")
    try:
        answers = [int(ans.strip()) for ans in user_answers.split(',')]
        if sorted(answers) == sorted([x1, x2]):
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answers are {x1} and {x2}\n")
    except:
        print(f"Invalid input. Correct answers are {x1} and {x2}\n")

def main():
    print("Welcome to Algebra Problem Generator!\n")
    while True:
        print("1. Generate Linear Equation")
        print("2. Generate Quadratic Equation")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            generate_linear()
        elif choice == '2':
            generate_quadratic()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
