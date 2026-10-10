# Exercise 10: Asynchronous Programming & Concurrency

## Objective

Master asynchronous I/O with Python's built-in `asyncio` module. Learn non-blocking execution, coroutines, concurrent task gathering, and timeout guardrails used in high-throughput AI API orchestration.

## Key Concepts

- `async def` defines a coroutine; `await` suspends it while asynchronous work completes.
- `asyncio.run()` creates and manages an event loop for a top-level asynchronous program.
- `asyncio.gather(*tasks)` runs independent awaitables concurrently and returns results in input order.
- `asyncio.wait_for(coro, timeout)` applies a deadline and raises `TimeoutError` when the operation exceeds it.
- `time.perf_counter()` measures elapsed wall-clock time for the concurrency demonstration.
- Asynchronous I/O concurrency is not the same as CPU-bound parallel execution. This exercise simulates network latency and does not call real model providers.

## Commands

Run the solution CLI from the repository root:

```bash
python exercises/10_asyncio_concurrency/solution.py
```

Run Exercise 10 tests:

```bash
python -m pytest exercises/10_asyncio_concurrency/test_solution.py
```

Run the complete test suite:

```bash
python -m pytest
```

## Implementation Overview

### `fetch_mock_model_response(model_id, prompt, delay=0.05)`

Simulates a provider request by awaiting `asyncio.sleep()`. It returns a dictionary with the model ID, prompt, success status, estimated token count, and simulated latency. Token count is a simple educational estimate, not a provider-reported usage metric.

### `execute_parallel_queries(requests)`

Builds one coroutine per request and passes them to `asyncio.gather()`. The operations overlap while waiting, while the returned result list preserves the order of the input requests. Each request may override the default delay.

### `fetch_with_timeout(model_id, prompt, timeout, delay)`

Wraps a simulated request with `asyncio.wait_for()`. If the deadline is exceeded, the call raises `TimeoutError`; the waiting coroutine is cancelled by the timeout mechanism.

### CLI demonstration

The CLI dispatches three mock model requests, measures total elapsed time, and prints each result's model ID, simulated latency, and token estimate. The measured elapsed time can vary across machines and CI runners.

## Example Output

The elapsed time is environment-dependent; output will resemble:

```text
--- AsyncIO Parallel Execution (50% Milestone) ---
Dispatched 3 concurrent model queries in 0.0400s.
- [deepseek-r1] latency: 0.04s, tokens: 13
- [llama-3.3-70b] latency: 0.03s, tokens: 13
- [gemini-2.0-flash] latency: 0.02s, tokens: 12
```

## Automated Test Coverage

The pytest suite verifies:

- A single mock model response and token estimate.
- Concurrent execution of multiple requests and input-order result preservation.
- A request that completes within its timeout.
- A request that exceeds its timeout and raises `asyncio.TimeoutError`.
- CLI execution and its key output.

## Practical Notes

- Use asyncio for workloads dominated by waiting on network, disk, or other asynchronous I/O.
- Coroutines do not make CPU-heavy Python code run in parallel by themselves; CPU-bound workloads may require processes or native code that releases the GIL.
- Keep timeouts aligned with realistic service-level objectives and account for cancellation behavior.
- For production fan-out, consider bounded concurrency, retries with backoff, provider rate limits, partial failures, and structured logging.
- The mock functions in this exercise are educational simulations, not live API integrations.
