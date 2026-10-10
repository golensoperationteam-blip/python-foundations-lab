import importlib.util
import os
import time
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location("exercise11_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
ExecutionTimer = _solution.ExecutionTimer
temp_env_var = _solution.temp_env_var


def test_execution_timer_records_duration():
    with ExecutionTimer() as timer:
        time.sleep(0.01)
    assert timer.elapsed is not None
    assert timer.elapsed >= 0.01


def test_execution_timer_does_not_suppress_exceptions():
    with pytest.raises(RuntimeError, match="boom"):
        with ExecutionTimer():
            raise RuntimeError("boom")


def test_temp_env_var_restores_original_value(monkeypatch):
    monkeypatch.setenv("FOUNDATIONS_TEMP_TEST", "original")
    with temp_env_var("FOUNDATIONS_TEMP_TEST", "temporary"):
        assert os.environ["FOUNDATIONS_TEMP_TEST"] == "temporary"
    assert os.environ["FOUNDATIONS_TEMP_TEST"] == "original"


def test_temp_env_var_removes_new_variable(monkeypatch):
    monkeypatch.delenv("FOUNDATIONS_TEMP_NEW", raising=False)
    with temp_env_var("FOUNDATIONS_TEMP_NEW", "temporary"):
        assert os.environ["FOUNDATIONS_TEMP_NEW"] == "temporary"
    assert "FOUNDATIONS_TEMP_NEW" not in os.environ
