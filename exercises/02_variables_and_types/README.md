# Exercise 2 — Variables and Types

## Objective

Practice Python variable values and built-in types by accepting typed values, deriving a boolean value, returning a dictionary, and testing both values and types.

## Function signature

Implement:

```python
def build_profile(name, age, height):
    ...
```

## Return structure

The function returns a dictionary with exactly these keys:

```python
{
    "name": name,
    "age": age,
    "height": height,
    "is_adult": age >= 18,
}
```

`is_adult` is `True` when `age` is at least 18 and `False` otherwise. The supplied `name`, `age`, and `height` values are preserved.

## Example usage

```python
build_profile("Alice", 25, 165.5)
```

Expected result:

```text
{'name': 'Alice', 'age': 25, 'height': 165.5, 'is_adult': True}
```

## CLI command

From the repository root:

```bash
python exercises/02_variables_and_types/solution.py
```

Expected output:

```text
{'name': 'World', 'age': 18, 'height': 170.5, 'is_adult': True}
```

## Test command

From the repository root:

```bash
python -m pytest exercises/02_variables_and_types/test_solution.py
```

The exercise tests adult and under-18 ages, boundary ages, zero values, decimal heights, empty and formatted names, exact dictionary keys, values, expected types, and the actual CLI output.

## Concepts demonstrated

- Variable assignment and function parameters
- Strings (`str`)
- Integers (`int`)
- Floating-point values (`float`)
- Booleans (`bool`)
- Boolean comparisons with `>=`
- Dictionary construction and access
- `isinstance()` for type checks in tests
- `if __name__ == "__main__":` as the script entry point
- Basic pytest assertions

## Edge cases

The tests cover:

- Age `0`
- Age `17`
- Age `18`
- Height `0.0`
- Decimal heights
- Empty names
- Names containing spaces
- Names containing punctuation

## Implementation assumptions

- `name`, `age`, and `height` are preserved exactly as supplied.
- `is_adult` is calculated only as `age >= 18`.
- The returned dictionary contains only `name`, `age`, `height`, and `is_adult`.
- No validation or conversion is added for invalid input types.
- The CLI entry point uses `build_profile("World", 18, 170.5)`.
- No additional dependencies are required beyond the repository's existing pytest development dependency.
