"""Reusable context managers for timing and temporary environment changes."""
from contextlib import contextmanager
import os
import time
from typing import Iterator, Optional


class ExecutionTimer:
    """Measure elapsed wall-clock time for a with-block."""

    def __init__(self) -> None:
        self.elapsed: Optional[float] = None
        self._started: Optional[float] = None

    def __enter__(self) -> "ExecutionTimer":
        self._started = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self._started is not None:
            self.elapsed = time.perf_counter() - self._started
        # Never suppress exceptions raised inside the managed block.
        return False


@contextmanager
def temp_env_var(key: str, value: str) -> Iterator[None]:
    """Set an environment variable temporarily and restore its prior state."""
    if not key:
        raise ValueError("Environment variable key must not be empty")
    existed = key in os.environ
    previous = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if existed:
            os.environ[key] = previous  # type: ignore[assignment]
        else:
            os.environ.pop(key, None)
