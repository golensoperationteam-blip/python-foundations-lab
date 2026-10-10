# python-foundations-lab

An evidence-driven Python fundamentals learning lab.

## Purpose

This repository is used to learn and document practical Python skills through:

- Small executable exercises
- Automated tests
- Command-line practice
- Clear technical notes
- Disciplined Git and GitHub workflows

This repository is evidence-generation infrastructure. Its existence does not automatically prove Python expertise.

## Learning Objectives

- Python syntax and basic data types
- Conditions, loops, and functions
- Lists, tuples, dictionaries, and sets
- Basic searching and sorting algorithms
- File I/O and JSON serialization
- Object-oriented programming with classes and composition
- Function decorators, execution profiling, and retry-based resilience
- Testing with pytest
- Command-line execution
- Reproducible documentation
- Feature branches, commits, pull requests, and merges

## Requirements

- Python 3.x
- Git
- A command-line terminal

## Current Progress

- Exercises completed: 8/20 (40%)
- Tests: Exercises 1 through 8 have automated test coverage
- Python level: Not yet evaluated

## Evidence Policy

Skill levels will be updated only after reviewing actual evidence such as:

- Working Python code
- Tests that run successfully
- Command-line execution
- Explanations and notes
- Meaningful commits
- Pull requests and review results
- Reproducible setup instructions

Completing this repository alone does not automatically establish a Python skill level.

## Planned Structure

```text
python-foundations-lab/
├── README.md
├── pyproject.toml
├── requirements-dev.txt
├── .gitignore
├── LICENSE
├── src/
│   └── python_foundations/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── exercises/
├── notes/
└── .github/
    └── workflows/
        └── tests.yml
```

## Learning Workflow

```text
Learn concept
    ↓
Implement exercise
    ↓
Write tests
    ↓
Run from the command line
    ↓
Document what was learned
    ↓
Commit focused changes
    ↓
Open pull request
    ↓
Review and merge
    ↓
Verify on main
```

## Planned Exercises

1. Hello Python
2. Variables and Types
3. Simple Calculator
4. Temperature Converter
5. Even or Odd
6. Positive, Negative, or Zero
7. Largest of Three Numbers
8. Multiplication Table
9. Sum of Numbers
10. Count Vowels
11. Reusable Calculator Functions
12. List Statistics
13. Remove Duplicates
14. Word Frequency Counter
15. Simple Contact Book
16. Linear Search
17. Binary Search
18. Bubble Sort
19. Palindrome Checker
20. Prime Number Checker

## Testing

Tests are written with pytest. The suite should cover:

- Normal inputs
- Boundary values
- Empty inputs
- Invalid inputs where applicable
- Expected exceptions
- Command-line execution
- Previously discovered bugs

Run all tests from the repository root:

```bash
python -m pytest
```

Run Exercise 06 independently:

```bash
python -m pytest exercises/06_json_io/test_solution.py
```

Run Exercise 07 independently:

```bash
python -m pytest exercises/07_oop_task_manager/test_solution.py
```

Run Exercise 08 independently:

```bash
python -m pytest exercises/08_decorators_and_retry/test_solution.py
```

## Git Workflow

Meaningful changes should follow this workflow:

```text
feature branch → implementation → tests → review → pull request → merge → verification
```

Suggested commit examples:

```text
feat: add calculator exercise
test: add calculator test coverage
docs: document Python setup
ci: add automated test workflow
```

## Status

The repository is initialized for Version 1. Exercises, tests, and notes are added progressively. No Python skill level has been assigned yet.

## CI Behavior

The GitHub Actions workflow runs pytest and treats pytest's exit code 5 (no tests collected) as a successful initial state, while still failing the job for actual test failures. The exercise progress above tracks the implemented learning exercises; CI status should be verified from the corresponding workflow run.
