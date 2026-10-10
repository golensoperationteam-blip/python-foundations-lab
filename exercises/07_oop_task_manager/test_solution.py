import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

# Load solution safely avoiding Python module digit naming issue
solution_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution_mod", solution_path)
solution_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_mod)

Task = solution_mod.Task
TaskManager = solution_mod.TaskManager
TaskNotFoundError = solution_mod.TaskNotFoundError


def test_task_creation_and_defaults():
    task = Task("T-100", "Run Benchmark", priority=2)
    assert task.task_id == "T-100"
    assert task.title == "Run Benchmark"
    assert task.status == "pending"
    assert task.priority == 2


def test_task_empty_fields_raise_error():
    with pytest.raises(ValueError):
        Task("", "Title")
    with pytest.raises(ValueError):
        Task("ID", "")


def test_task_status_transition():
    task = Task("T-101", "Code Audit")
    task.set_status("in_progress")
    assert task.status == "in_progress"
    task.mark_completed()
    assert task.status == "completed"
    with pytest.raises(ValueError):
        task.set_status("unknown_status")


def test_task_dict_roundtrip():
    original = Task("T-102", "Write Docs", priority=3)
    original.mark_completed()
    d = original.to_dict()
    reconstructed = Task.from_dict(d)
    assert reconstructed.task_id == original.task_id
    assert reconstructed.title == original.title
    assert reconstructed.status == "completed"


def test_task_manager_add_and_get():
    mgr = TaskManager()
    t = Task("T-1", "Task One")
    mgr.add_task(t)
    assert mgr.get_task("T-1") is t
    with pytest.raises(TaskNotFoundError):
        mgr.get_task("NON_EXISTENT")


def test_task_manager_duplicate_id_raises_error():
    mgr = TaskManager()
    t1 = Task("T-1", "Task One")
    t2 = Task("T-1", "Duplicate ID Task")
    mgr.add_task(t1)
    with pytest.raises(ValueError):
        mgr.add_task(t2)


def test_task_manager_list_and_filter():
    mgr = TaskManager()
    t1 = Task("T-1", "Pending Task")
    t2 = Task("T-2", "Completed Task")
    t2.mark_completed()
    mgr.add_task(t1)
    mgr.add_task(t2)
    assert len(mgr.list_tasks()) == 2
    completed = mgr.list_tasks(status="completed")
    assert len(completed) == 1
    assert completed[0].task_id == "T-2"


def test_cli_execution():
    cmd = [sys.executable, str(solution_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "OOP Task Manager Initialized: 2 tasks tracked." in res.stdout
