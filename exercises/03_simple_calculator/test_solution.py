import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


def _load_solution():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_03_solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


calculate = _load_solution().calculate


def test_addition_positive_values():
    assert calculate(10, 5, "+") == 15


def test_addition_negative_values():
    assert calculate(-10, -5, "+") == -15


def test_addition_decimal_values():
    assert calculate(1.5, 2.5, "+") == 4.0


def test_subtraction_negative_result():
    assert calculate(5, 10, "-") == -5


def test_subtraction_negative_values():
    assert calculate(-5, -10, "-") == 5


def test_multiplication_includes_zero():
    assert calculate(10, 0, "*") == 0


def test_multiplication_negative_values():
    assert calculate(-4, 3, "*") == -12


def test_multiplication_decimal_values():
    assert calculate(2.5, 2, "*") == 5.0


def test_division_normal_result():
    assert calculate(10, 2, "/") == 5.0


def test_division_decimal_result():
    assert calculate(5, 2, "/") == 2.5


def test_division_by_one():
    assert calculate(7, 1, "/") == 7.0


def test_zero_divided_by_nonzero():
    assert calculate(0, 5, "/") == 0.0


def test_division_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        calculate(10, 0, "/")


def test_unsupported_operation_raises_value_error():
    with pytest.raises(ValueError):
        calculate(10, 5, "%")


def test_empty_operation_raises_value_error():
    with pytest.raises(ValueError):
        calculate(10, 5, "")


def test_cli_output():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("solution.py"))],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "15"
