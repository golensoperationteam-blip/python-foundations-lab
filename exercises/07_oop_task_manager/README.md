# Exercise 07: Object-Oriented Programming (OOP) — Agent Task Manager

## Objective
Understand core Object-Oriented Programming (OOP) principles in Python: classes, instance attributes, encapsulation, class methods, object composition, and custom exceptions.

## Key Concepts
- `class` definitions with `__init__`, instance methods, and `self`
- Encapsulation and state validation through `VALID_STATUSES`
- `@classmethod` factory methods (`from_dict`) for object reconstruction
- Object composition: `TaskManager` manages instances of `Task`
- Custom exception design with `TaskNotFoundError`
- String representations through `__repr__`
- Serialization-friendly object conversion using `to_dict` and `from_dict`

## Commands
Run the solution CLI from the repository root:

```bash
python exercises/07_oop_task_manager/solution.py
```

Run Exercise 07 tests:

```bash
python -m pytest exercises/07_oop_task_manager/test_solution.py
```

Run the complete test suite:

```bash
python -m pytest
```

## Design Overview

### `Task`
Represents one unit of work. Each task has an ID, title, integer priority, and status. New tasks begin as `pending`. The supported statuses are `pending`, `in_progress`, and `completed`. Invalid status transitions raise `ValueError`.

- `set_status(new_status)`: validates and changes task status.
- `mark_completed()`: marks the task completed.
- `to_dict()`: returns a dictionary representation.
- `from_dict(data)`: reconstructs a task from a dictionary.
- `__repr__()`: provides a useful developer-facing representation.

### `TaskManager`
Stores `Task` objects in an internal dictionary keyed by task ID.

- `add_task(task)`: adds a task and rejects duplicate IDs with `ValueError`.
- `get_task(task_id)`: returns a task or raises `TaskNotFoundError`.
- `list_tasks(status=None)`: returns all tasks, optionally filtered by status.
- `total_count()`: returns the number of managed tasks.

## Example
The command-line demo creates two tasks, marks “Inspect Model Registry” as completed, and prints the task count and completed task titles.

## Automated Test Coverage
The pytest suite checks task construction and defaults, required fields, valid and invalid status changes, dictionary round-tripping, task lookup, missing-task errors, duplicate IDs, status filtering, and CLI execution.
