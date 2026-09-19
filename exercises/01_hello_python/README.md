# Exercise 1 — Hello Python

## Objective

Practice defining and calling a simple Python function, returning a string, running a Python file from the command line, and writing beginner-friendly pytest tests.

## Problem

Implement `greet(name)` so it returns a greeting in the form `Hello, <name>!`. The exercise also provides a command-line entry point that greets `World`.

## Run the program

From the repository root:

```bash
python exercises/01_hello_python/solution.py
```

Expected output:

```text
Hello, World!
```

## Run the tests

From the repository root:

```bash
python -m pytest exercises/01_hello_python/test_solution.py
```

The test suite checks ordinary names, an empty string, spaces, punctuation, a numeric value, the return type, and the actual command-line output.

## Concepts demonstrated

- Function definition with `def`
- Function parameters and return values
- String formatting with an f-string
- `print()` for command-line output
- `if __name__ == "__main__":` as the script entry point
- Basic pytest assertions
- Standard-library `subprocess` testing of a CLI program

## Implementation assumptions

- `greet(name)` formats the supplied value directly; it does not add unnecessary input validation.
- Ordinary strings, spaces, punctuation, and numeric values are supported by the formatting operation.
- The command-line entry point always calls `greet("World")`.
- No additional dependencies are required beyond the repository's existing pytest development dependency.
