# Exercise 09: Python Generators & Streaming Pipelines

## Objective

Understand lazy evaluation, memory-efficient streaming, the `yield` keyword, generator functions, and pipeline chaining used for real-time LLM token streaming and large dataset processing.

## Key Concepts

- `yield` vs `return`: suspended state execution.
- Lazy evaluation: values are produced on demand, avoiding the need to materialize the entire input.
- Chained generator pipelines (`filter_stream` over `stream_batches`).
- Standard type annotations with `typing.Generator` and `typing.Iterable`.
- Streaming tokenization simulation.

## Commands

Run the solution CLI from the repository root:

```bash
python exercises/09_generators_streaming/solution.py
```

Run Exercise 09 tests:

```bash
python -m pytest exercises/09_generators_streaming/test_solution.py
```

Run the complete test suite:

```bash
python -m pytest
```

## Implementation Overview

### `stream_batches(iterable, batch_size=10)`

Consumes any iterable incrementally and yields lists containing up to `batch_size` items. The final batch may be smaller than the requested size. A batch size below one raises `ValueError`. Memory use is bounded by the current batch rather than the size of the complete input.

### `filter_stream(stream, predicate)`

Lazily yields only values for which the supplied predicate returns true. It can be composed with other iterables and generator stages without first building an intermediate list.

### `token_stream_simulator(text)`

Splits sample text into words and yields each word with a trailing space to simulate incremental token output. This is an educational simulation, not a connection to a live language model.

## Example Output

The exact spacing and token text are deterministic:

```text
--- Simulating Streaming Tokens ---
Generated 10 stream tokens: Universal AI OS provides sovereign multi model routing and streaming verification

--- Batched Generator Stream (batch_size=10) ---
Batch 1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Batch 2: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Batch 3: [21, 22, 23, 24, 25]

Filtered Evens Stream Count: 12
```

## Automated Test Coverage

The pytest suite checks:

- Generator type and partial final batch behavior.
- Exact multiples of the batch size.
- Empty iterables.
- Rejection of an invalid batch size.
- Lazy filtering of even numbers.
- Expected tokens from the token simulator.
- CLI execution and key output.

## Practical Notes

- Generator functions execute as their values are requested; calling one returns a generator object rather than immediately running the full body.
- A generator is usually consumed once. Create a new generator when the same stream must be traversed again.
- Streaming reduces intermediate storage, but each retained batch still occupies memory.
- The CLI converts the streams to lists for demonstration. For genuinely large inputs, iterate directly over the generator to preserve the memory benefit.
- Generator pipelines are useful for log processing, ETL, large files, event streams, and incremental model output.
