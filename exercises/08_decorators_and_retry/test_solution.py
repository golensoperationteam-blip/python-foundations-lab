import importlib.util
import subprocess
import sys
import time
from pathlib import Path

import pytest

# Load solution dynamically to bypass digit-prefix import issue.
solution_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution_mod", solution_path)
solution_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_mod)

timed = solution_mod.timed
retry = solution_mod.retry


def test_timed_decorator_returns_result_and_duration():
    @timed
    def add(a, b):
        """Add two numbers."""
        time.sleep(0.01)
        return a + b

    result, duration = add(10, 20)
    assert result == 30
    assert duration >= 0.009
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."


def test_retry_decorator_successful_first_try():
    calls = 0

    @retry(max_attempts=3)
    def flawless():
        nonlocal calls
        calls += 1
        return "success"

    assert flawless() == "success"
    assert calls == 1


def test_retry_decorator_recovers_after_failures():
    attempts = 0

    @retry(max_attempts=3, delay=0.001, exceptions=(ValueError,))
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise ValueError("Temporary glitch")
        return "recovered"

    assert flaky() == "recovered"
    assert attempts == 2


def test_retry_decorator_raises_after_max_attempts():
    attempts = 0

    @retry(max_attempts=3, delay=0.001, exceptions=(RuntimeError,))
    def always_fails():
        nonlocal attempts
        attempts += 1
        raise RuntimeError("Permanent failure")

    with pytest.raises(RuntimeError) as exc_info:
        always_fails()
    assert "Permanent failure" in str(exc_info.value)
    assert attempts == 3


def test_retry_does_not_catch_unspecified_exceptions():
    @retry(max_attempts=3, exceptions=(ValueError,))
    def wrong_error():
        raise KeyError("Unexpected key error")

    with pytest.raises(KeyError):
        wrong_error()


def test_retry_invalid_max_attempts():
    with pytest.raises(ValueError):

        @retry(max_attempts=0)
        def dummy():
            pass


def test_cli_execution():
    cmd = [sys.executable, str(solution_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "Timing Profiler: Generated 150 tokens" in res.stdout
    assert "Retry Mechanism: API Call Succeeded" in res.stdout
