import subprocess
import sys
from pathlib import Path

from solution import greet


def test_greet_world():
    assert greet("World") == "Hello, World!"


def test_greet_alice():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_another_ordinary_name():
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


def test_greet_name_with_spaces():
    assert greet("Mary Jane") == "Hello, Mary Jane!"


def test_greet_name_with_punctuation():
    assert greet("Dr. Smith, Jr.") == "Hello, Dr. Smith, Jr.!"


def test_greet_number():
    assert greet(42) == "Hello, 42!"


def test_greet_returns_string():
    assert isinstance(greet("World"), str)


def test_cli_output():
    solution_path = Path(__file__).with_name("solution.py")
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ""
