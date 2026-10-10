import importlib.util
from pathlib import Path
from threading import Barrier

import pytest

_spec = importlib.util.spec_from_file_location("exercise16_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
parallel_process_tasks = _solution.parallel_process_tasks


def test_results_sorted_and_inputs_not_mutated():
    tasks = [{"id": "b", "value": 2}, {"id": "a", "value": 1}]
    results = parallel_process_tasks(tasks)
    assert [row["id"] for row in results] == ["a", "b"]
    assert [row["result"] for row in results] == [1, 2]
    assert all(row["processed"] for row in results)
    assert "processed" not in tasks[0]


def test_tasks_run_concurrently():
    barrier = Barrier(3, timeout=2)
    def work(_):
        barrier.wait()
        return "done"
    results = parallel_process_tasks([{"id": str(i), "run": work} for i in range(3)], max_workers=3)
    assert [row["result"] for row in results] == ["done"] * 3


def test_worker_exception_propagates():
    def fail(_):
        raise RuntimeError("worker failed")
    with pytest.raises(RuntimeError, match="worker failed"):
        parallel_process_tasks([{"id": "x", "run": fail}])


def test_invalid_inputs():
    with pytest.raises(ValueError):
        parallel_process_tasks([], max_workers=0)
    with pytest.raises(TypeError):
        parallel_process_tasks([1])
