# Exercise 08: Function Decorators, Profiling & Retry Logic

## Objective

Master advanced Python function decorators, closures, higher-order functions, and resilience patterns essential for AI agent observability and fault-tolerant network operations.

## Key Concepts

- Higher-order functions: functions returning functions.
- Closures and function wrapping using `*args` and `**kwargs`.
- Metadata preservation with `functools.wraps`.
- Parameterized decorators such as `@retry(...)`.
- Fault-tolerant retry loops with configurable delay and exception filters.
- Execution profiling with the high-precision monotonic clock `time.perf_counter`.

## Commands

Run the solution CLI from the repository root:

```bash
python exercises/08_decorators_and_retry/solution.py
```

Run Exercise 08 tests:

```bash
python -m pytest exercises/08_decorators_and_retry/test_solution.py
```

Run the complete test suite:

```bash
python -m pytest
```

## Design Overview

### `timed(func)`

Wraps a function, measures its elapsed execution time with `time.perf_counter()`, and returns a pair: `(result, elapsed_seconds)`. The `functools.wraps` decorator preserves the wrapped function's metadata, including its name and docstring.

### `retry(max_attempts, delay, exceptions)`

Creates a configurable decorator that retries calls when they raise one of the selected exception types. It returns immediately on success, waits between retry attempts, and re-raises the final matching exception when the attempt limit is reached. Invalid values where `max_attempts < 1` raise `ValueError`.

Only exceptions explicitly included in the `exceptions` tuple are retried. Other exceptions propagate immediately.

## Example

The command-line demonstration profiles a simulated inference call and retries a simulated API request that fails twice with `ConnectionError` before succeeding on the third attempt.

Example output (elapsed time may vary):

```text
Timing Profiler: Generated 150 tokens in 0.0501s
Retry Mechanism: API Call Succeeded after 3 attempts.
```

## Automated Test Coverage

The pytest suite verifies:

- Timed return values, elapsed duration, function name, and docstring.
- Retry behavior when the first attempt succeeds.
- Recovery after a transient failure.
- Re-raising the final exception after exhausting attempts.
- Immediate propagation of exceptions outside the configured filter.
- Validation of `max_attempts`.
- Command-line execution and expected output.

## Practical Notes

- Use monotonic clocks such as `time.perf_counter()` for duration measurement.
- Retries are most appropriate for transient failures; retrying permanent errors wastes time.
- Choose exception filters deliberately and avoid retrying errors that indicate invalid input.
- In production systems, consider exponential backoff, jitter, timeouts, cancellation, and idempotency for operations with side effects.
