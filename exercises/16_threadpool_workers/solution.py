"""Parallel task processing with a bounded thread pool."""
from concurrent.futures import ThreadPoolExecutor
from typing import Any


def _process_task(task: dict[str, Any]) -> dict[str, Any]:
    item = dict(task)
    runner = item.pop("run", None)
    if runner is not None:
        if not callable(runner):
            raise TypeError("task 'run' value must be callable")
        item["result"] = runner(item)
    else:
        item.setdefault("result", item.get("value"))
    item["processed"] = True
    return item


def parallel_process_tasks(tasks: list[dict], max_workers: int = 4) -> list[dict]:
    """Process tasks concurrently; sort output by task_id or id."""
    if max_workers < 1:
        raise ValueError("max_workers must be at least 1")
    if any(not isinstance(task, dict) for task in tasks):
        raise TypeError("every task must be a dictionary")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(_process_task, tasks))
    return sorted(results, key=lambda row: str(row.get("task_id", row.get("id", ""))))
