# Exercise 3 — Simple Calculator

## Objective

Practice functions, parameters, return values, conditional logic, arithmetic operations, and basic exception handling in Python.

## Function Signature

```python
def calculate(first, second, operation):
    ...
```

The function accepts two numbers and an operation string and returns the calculated result.

## Supported Operations

| Operation | Behavior |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |

## Examples

```python
calculate(10, 5, "+")  # 15
calculate(10, 5, "-")  # 5
calculate(10, 5, "*")  # 50
calculate(10, 5, "/")  # 2.0
```

Division uses Python's normal `/` operator and therefore returns a float result.

## Error Behavior

- Division by zero raises `ValueError`.
- An unsupported operation raises `ValueError`.
- An empty operation also raises `ValueError`.
- General input-type validation is intentionally outside the scope of this beginner exercise.

## CLI Command and Output

Run:

```bash
python exercises/03_simple_calculator/solution.py
```

Output:

```text
15
```

The script uses a fixed example call so the exercise can be verified directly from the command line. It does not use interactive input or advanced CLI parsing.

## Test Command

Run the Exercise 3 tests:

```bash
python -m pytest exercises/03_simple_calculator/test_solution.py
```

Run the full repository test suite:

```bash
python -m pytest
```

## Concepts Demonstrated

- Function definition and calls
- Multiple function parameters
- Return values
- `if`/`elif`/`else` branching
- Arithmetic with integers and floats
- Raising `ValueError`
- Automated testing with pytest
- Command-line execution

## Edge Cases Tested

The tests cover:

- Positive, negative, and decimal addition
- Subtraction producing a negative result
- Multiplication by zero
- Multiplication with negative values
- Normal division and decimal results
- Division by one
- Zero divided by a nonzero number
- Division by zero
- Unsupported operations
- Empty operations
- Actual CLI output
