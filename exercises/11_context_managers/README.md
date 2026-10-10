# Exercise 11: Context Managers

## Objective
Use context managers to manage setup/cleanup reliably, measure execution duration, and temporarily change process environment state.

## Concepts
- `__enter__` prepares a managed block and can return an object used by the caller.
- `__exit__` runs when the block exits, including when an exception is raised.
- Returning `True` from `__exit__` suppresses an exception; this timer intentionally returns `False`.
- `contextlib.contextmanager` turns a generator into a context manager; `finally` guarantees restoration.
- Environment variables are process-global, so temporary changes should be scoped and restored.

## Implementation
`ExecutionTimer` exposes `elapsed` after the block exits, measured with `time.perf_counter()`. `temp_env_var(key, value)` restores an existing value or removes a variable that did not previously exist.

## Run
```bash
python -m pytest exercises/11_context_managers/test_solution.py
```

## Coverage
Tests validate elapsed duration, exception propagation, restoration of an existing variable, and cleanup of a newly created variable.
