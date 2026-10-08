import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


def _load_solution():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_04_solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


analyze_numbers = _load_solution().analyze_numbers


def test_positive_integers():
    assert analyze_numbers([2, 4, 6, 8]) == {
        "count": 4,
        "sum": 20,
        "average": 5.0,
        "min": 2,
        "max": 8,
        "evens": [2, 4, 6, 8],
    }


def test_negative_integers():
    assert analyze_numbers([-5, -4, -3, -2]) == {
        "count": 4,
        "sum": -14,
        "average": -3.5,
        "min": -5,
        "max": -2,
        "evens": [-4, -2],
    }


def test_floats():
    result = analyze_numbers([1.5, 2.5, 3.5])
    assert result["count"] == 3
    assert result["sum"] == 7.5
    assert result["average"] == 2.5
    assert result["min"] == 1.5
    assert result["max"] == 3.5
    assert result["evens"] == []


def test_single_element_list():
    assert analyze_numbers([7]) == {
        "count": 1,
        "sum": 7,
        "average": 7.0,
        "min": 7,
        "max": 7,
        "evens": [],
    }


def test_mixed_integers_and_floats():
    assert analyze_numbers([2, 3.5, 4, -1.5, 6]) == {
        "count": 5,
        "sum": 14.0,
        "average": 2.8,
        "min": -1.5,
        "max": 6,
        "evens": [2, 4, 6],
    }


def test_non_integral_floats_are_not_even():
    result = analyze_numbers([2.5, 3.0, 4.5, -2.5])
    assert result["evens"] == []


def test_even_integers_preserve_input_order():
    result = analyze_numbers([9, 4, -2, 7, 6, 3])
    assert result["evens"] == [4, -2, 6]


def test_exact_return_keys():
    result = analyze_numbers([1, 2])
    assert set(result.keys()) == {"count", "sum", "average", "min", "max", "evens"}


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        analyze_numbers([])


def test_cli_output():
    solution_path = Path(__file__).with_name("solution.py")
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "List analysis:" in result.stdout
    assert "Input: [4, -3, 2.5, 8, 7]" in result.stdout
    assert "'count': 5" in result.stdout
    assert "'sum': 18.5" in result.stdout
    assert "'average': 3.7" in result.stdout
    assert "'min': -3" in result.stdout
    assert "'max': 8" in result.stdout
    assert "'evens': [4, 8]" in result.stdout
    assert result.stderr == ""
