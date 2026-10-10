import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


def _load_solution():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_06_solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution


_solution = _load_solution()
save_json = _solution.save_json
load_json = _solution.load_json


def test_save_and_load_roundtrip(tmp_path):
    test_file = tmp_path / "test_config.json"
    data = {"project": "universal-ai-os", "active": True, "count": 42, "items": ["a", "b"]}
    assert save_json(test_file, data) is True
    loaded = load_json(test_file)
    assert loaded == data


def test_save_creates_parent_directories(tmp_path):
    nested_file = tmp_path / "nested" / "deep" / "config.json"
    data = {"nested": True}
    assert save_json(nested_file, data) is True
    assert load_json(nested_file) == data


def test_load_non_existent_file(tmp_path):
    missing_file = tmp_path / "does_not_exist.json"
    with pytest.raises(FileNotFoundError):
        load_json(missing_file)


def test_load_corrupted_json(tmp_path):
    corrupt_file = tmp_path / "corrupt.json"
    corrupt_file.write_text("{this is not valid json:", encoding="utf-8")
    with pytest.raises(ValueError):
        load_json(corrupt_file)


def test_save_non_serializable_type(tmp_path):
    target_file = tmp_path / "fail.json"
    unsupported_data = {"key": {1, 2, 3}}  # set is not JSON serializable
    with pytest.raises(TypeError):
        save_json(target_file, unsupported_data)


def test_cli_execution():
    solution_path = Path(__file__).with_name("solution.py")
    cmd = [sys.executable, str(solution_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "JSON I/O Successful: Agent 'JARVIS' loaded" in res.stdout
    assert res.stderr == ""
