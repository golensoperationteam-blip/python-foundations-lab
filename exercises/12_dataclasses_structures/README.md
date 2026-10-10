# Exercise 12: Modern Dataclasses

## Objective
Represent model evaluation results as validated Python records and serialize them as JSON.

## Concepts
- `@dataclass` generates common data-model methods.
- `order=True` generates ordering based on field declaration order; it does not automatically sort by score alone.
- `__post_init__` enforces invariants after initialization.
- JSON serialization creates a portable representation for files and APIs.
- Round-trip tests confirm data can be encoded and reconstructed.

## Implementation
`ModelBenchmark` stores `model_id`, `score`, and `eval_date`; scores must be in the inclusive range 0–100. Use `to_json()` and `from_json()` to serialize and restore records.

## Run
```bash
python -m pytest exercises/12_dataclasses_structures/test_solution.py
```

## Coverage
Tests cover score sorting, invalid boundaries, and JSON round trips at lower, middle, and upper valid scores.
