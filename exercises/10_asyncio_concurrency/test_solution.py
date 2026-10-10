import asyncio
import importlib.util
import subprocess
import sys
import time
import pytest
from pathlib import Path

solution_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution_mod", solution_path)
solution_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_mod)

fetch_mock_model_response = solution_mod.fetch_mock_model_response
execute_parallel_queries = solution_mod.execute_parallel_queries
fetch_with_timeout = solution_mod.fetch_with_timeout

def test_fetch_single_model():
    res = asyncio.run(fetch_mock_model_response("test-model", "hello world", delay=0.01))
    assert res["model_id"] == "test-model"
    assert res["status"] == "success"
    assert res["tokens"] == 12

def test_parallel_queries_concurrency():
    queries = [
        {"model_id": "m1", "prompt": "p1", "delay": 0.03},
        {"model_id": "m2", "prompt": "p2", "delay": 0.03},
        {"model_id": "m3", "prompt": "p3", "delay": 0.03}
    ]
    start = time.perf_counter()
    results = asyncio.run(execute_parallel_queries(queries))
    elapsed = time.perf_counter() - start

    assert len(results) == 3
    # If executed sequentially it would take >= 0.09s. Concurrently it should take ~0.03s-0.06s.
    assert elapsed < 0.08
    assert [r["model_id"] for r in results] == ["m1", "m2", "m3"]

def test_timeout_success():
    res = asyncio.run(fetch_with_timeout("fast-model", "test", timeout=0.1, delay=0.01))
    assert res["status"] == "success"

def test_timeout_triggered():
    with pytest.raises(asyncio.TimeoutError):
        asyncio.run(fetch_with_timeout("slow-model", "test", timeout=0.01, delay=0.05))

def test_cli_execution():
    cmd = [sys.executable, str(solution_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "AsyncIO Parallel Execution (50% Milestone)" in res.stdout
    assert "Dispatched 3 concurrent model queries" in res.stdout
