import importlib.util
import subprocess
import sys
from pathlib import Path


def _load_solution():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_05_solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


count_words = _load_solution().count_words


def test_basic_sentence():
    assert count_words("Python is fun") == {
        "python": 1,
        "is": 1,
        "fun": 1,
    }


def test_repeated_words():
    assert count_words("red blue red red blue") == {
        "red": 3,
        "blue": 2,
    }


def test_default_case_insensitive_behavior():
    assert count_words("Python python PYTHON") == {"python": 3}


def test_case_sensitive_behavior():
    assert count_words("Python python PYTHON", case_sensitive=True) == {
        "Python": 1,
        "python": 1,
        "PYTHON": 1,
    }


def test_punctuation_removal_enabled():
    assert count_words("Hello, hello! Hello.") == {"hello": 3}


def test_punctuation_preservation_when_disabled():
    assert count_words("Hello, hello!", remove_punctuation=False) == {
        "hello,": 1,
        "hello!": 1,
    }


def test_empty_string():
    assert count_words("") == {}


def test_whitespace_only_string():
    assert count_words("   \t\n  ") == {}


def test_mixed_punctuation():
    assert count_words('Well, "hello"; well? (hello).') == {
        "well": 2,
        "hello": 2,
    }


def test_punctuation_removal_preserves_word_boundaries():
    assert count_words("hello,world") == {
        "hello": 1,
        "world": 1,
    }


def test_deterministic_word_counts():
    text = "One, two one; TWO three."
    expected = {"one": 2, "two": 2, "three": 1}
    assert count_words(text) == expected
    assert count_words(text) == expected


def test_cli_execution_and_output():
    solution_path = Path(__file__).with_name("solution.py")
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Word frequency:" in result.stdout
    assert "Input: Python is fun, and Python is practical!" in result.stdout
    assert "'python': 2" in result.stdout
    assert "'is': 2" in result.stdout
    assert "'fun': 1" in result.stdout
    assert "'and': 1" in result.stdout
    assert "'practical': 1" in result.stdout
    assert result.stderr == ""
