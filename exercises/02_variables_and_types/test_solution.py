import importlib.util
import subprocess
import sys
from pathlib import Path


def _load_solution():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_02_solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


build_profile = _load_solution().build_profile


def test_adult_age():
    assert build_profile("Alice", 25, 165.5)["is_adult"] is True


def test_under_18_age():
    assert build_profile("Bob", 17, 170.0)["is_adult"] is False


def test_age_18_boundary():
    assert build_profile("Boundary", 18, 180.0)["is_adult"] is True


def test_age_17_boundary():
    assert build_profile("Boundary", 17, 180.0)["is_adult"] is False


def test_age_zero_and_height_zero():
    assert build_profile("Zero", 0, 0.0) == {
        "name": "Zero",
        "age": 0,
        "height": 0.0,
        "is_adult": False,
    }


def test_decimal_height_is_preserved():
    result = build_profile("Alice", 25, 165.75)
    assert result["height"] == 165.75


def test_empty_name():
    assert build_profile("", 25, 165.5)["name"] == ""


def test_name_with_spaces():
    assert build_profile("Mary Jane", 25, 165.5)["name"] == "Mary Jane"


def test_name_with_punctuation():
    assert build_profile("Dr. Smith, Jr.", 25, 165.5)["name"] == "Dr. Smith, Jr."


def test_exact_dictionary_keys():
    result = build_profile("Alice", 25, 165.5)
    assert set(result.keys()) == {"name", "age", "height", "is_adult"}


def test_values_are_preserved_and_is_adult_is_derived():
    result = build_profile("Alice", 25, 165.5)
    assert result["name"] == "Alice"
    assert result["age"] == 25
    assert result["height"] == 165.5
    assert result["is_adult"] is True


def test_expected_types():
    result = build_profile("Alice", 25, 165.5)
    assert isinstance(result["name"], str)
    assert isinstance(result["age"], int)
    assert isinstance(result["height"], float)
    assert isinstance(result["is_adult"], bool)


def test_cli_output():
    solution_path = Path(__file__).with_name("solution.py")
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "{'name': 'World', 'age': 18, 'height': 170.5, 'is_adult': True}\n"
    assert result.stderr == ""
