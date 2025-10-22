# 🧮 Algebra Problem Generator

A small, interactive Python script that generates random algebra practice problems (linear and simple quadratic equations) and lets the user attempt solutions with immediate feedback.

## Contents

- `algebra_generator.py` — interactive script that generates problems and checks user answers.

## Features

- Generate random linear equations (one variable)
- Generate random simple quadratic equations with integer roots
- Immediate self-check/feedback for answers
- Small and easy to extend

## Requirements

- Python 3.8 or newer

The script uses only the Python standard library (module `random`). No extra packages are required.

## Quick start (PowerShell / Windows)

1. Clone the repo and change into the folder:

```powershell
git clone https://github.com/LaxmiPrasad-Konduri/algebra-problem-generator.git ;
cd algebra-problem-generator
```

2. Run the generator:

```powershell
python .\algebra_generator.py
```

If you are using a virtual environment, activate it first (recommended):

```powershell
python -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; python .\algebra_generator.py
```

## Usage

When you run `algebra_generator.py` you'll see a simple menu:

1. Generate Linear Equation
2. Generate Quadratic Equation
3. Exit

- Linear equation format: `ax + b = c`. The script computes a solution `x` and prompts you to enter it as a number (e.g. `5` or `5.0`).
- Quadratic equation format: `x^2 + (b)x + (c) = 0` where the script generates integer roots. For quadratics you should enter both integer solutions separated by a comma (for example: `2, 5`). Order does not matter.

Example session (user input shown after prompts):

```
Welcome to Algebra Problem Generator!

1. Generate Linear Equation
2. Generate Quadratic Equation
3. Exit
Choose an option (1-3): 1
Solve for x: 3x + 4 = 19
Your answer: 5
Correct!

Choose an option (1-3): 2
Solve for x: x^2 + (-7)x + (12) = 0
Enter both solutions separated by comma: 3,4
Correct!
```

## Notes & edge cases

- The linear generator expects a numeric answer. Non-numeric input will raise a ValueError when converting to `float`.
- The quadratic generator expects two integer roots separated by a comma. Non-integer or incorrectly formatted input will be reported as invalid and the correct roots printed.
- The script is intended for small practice sessions and for educational/learning use. It is not designed as a production assessment tool.

## Contributing

Small improvements, bug fixes and additional problem types are welcome. Please open issues or pull requests on the repository.

## License

This project includes a `LICENSE` file. See that file for license terms.

## Author

LaxmiPrasad Konduri
