# Exercise 4 — List Analyzer

## Objective

Practice working with lists, loops, list comprehensions, functions, and basic statistics in Python.

## Function Signature

```python
def analyze_numbers(numbers: list[int | float]) -> dict:
    ...
```

The function analyzes a non-empty list of integers and/or floats.

## Expected Return Fields

The returned dictionary contains exactly these keys:

| Field | Meaning |
|---|---|
| `count` | Number of input values |
| `sum` | Total of all input values |
| `average` | Arithmetic average |
| `min` | Minimum value |
| `max` | Maximum value |
| `evens` | Even integer values, preserving input order |

Non-integral floats are not classified as even. The `evens` list contains integer values only.

## Error Behavior

An empty input list raises `ValueError` because statistics such as minimum and maximum are undefined for an empty list.

## Concepts Demonstrated

- **Loops:** Process values in a list and reason about repeated data.
- **List comprehensions:** Build the `evens` list concisely while preserving input order.
- **Basic statistics:** Calculate count, sum, average, minimum, and maximum using Python's built-in operations.
- **Functions:** Keep the analysis reusable and separate from command-line output.
- **Dictionaries:** Return the analysis using named fields.

## CLI Command

Run the sample analysis from the repository root:

```bash
python exercises/04_list_analyzer/solution.py
```

The CLI demonstrates the function with a sample list and prints the input and resulting analysis clearly.

## Test Command

Run the Exercise 4 tests:

```bash
python -m pytest exercises/04_list_analyzer/test_solution.py
```

Run the full repository test suite:

```bash
python -m pytest
```

## Validation Scope

The tests cover positive integers, negative integers, floats, a single-element list, mixed numeric values, all required statistics, even-integer filtering and ordering, empty-list error handling, and CLI output.
