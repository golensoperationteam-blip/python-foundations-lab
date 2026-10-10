# Exercise 06: File I/O & JSON Persistence

## Objective
Master safe file reading and writing using Python's standard-library `json` and `pathlib.Path`. Learn to handle missing files and malformed JSON payloads.

## Key Concepts
- `pathlib.Path` for cross-platform path manipulation and parent-directory creation
- `json.dumps()` / `json.loads()` for serialization and deserialization
- UTF-8 file encoding and two-space JSON indentation
- Exception handling: `FileNotFoundError`, `ValueError`, and `TypeError`
- Isolated automated testing with pytest's `tmp_path` fixture

## Commands

Run the solution CLI from the repository root:

```bash
python exercises/06_json_io/solution.py
```

Run the exercise tests:

```bash
python -m pytest exercises/06_json_io/test_solution.py
```

Run the complete test suite:

```bash
python -m pytest
```

## Functions

### `save_json(filepath, data) -> bool`
Creates missing parent directories, serializes a dictionary or list as JSON with two-space indentation, writes using UTF-8, and returns `True`. Unsupported values raise `TypeError`.

### `load_json(filepath) -> JsonData`
Reads and parses a JSON file. A missing file raises `FileNotFoundError`; malformed JSON raises `ValueError`.

## Example

The CLI writes a temporary `demo_agent_memory.json` file containing sample JARVIS metadata, reads it back, prints a success message, and removes the demo file.

The automated tests cover round-trip persistence, nested directory creation, missing files, corrupted JSON, non-serializable values, and CLI execution.
