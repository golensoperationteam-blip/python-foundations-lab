# Exercise 15: CLI Subcommands

## Objective
Build a command-line interface with independent subcommands for benchmark records and task routing.

## Concepts
- `argparse.ArgumentParser` defines CLI syntax and validation.
- Subparsers provide separate command-specific arguments.
- Exit codes let shell scripts and CI detect failure.
- Small routing rules can map task descriptions to stable categories.
- Input validation should reject invalid benchmark scores before formatting output.

## Usage
```bash
python exercises/15_cli_subcommands/solution.py bench --model deepseek-r1 --score 92.5
python exercises/15_cli_subcommands/solution.py route --task "debug this Python function"
python -m pytest exercises/15_cli_subcommands/test_solution.py
```

## Output
```text
Benchmark: model=deepseek-r1, score=92.5/100
Route: coding
```

## Coverage
Subprocess tests assert successful exit codes and expected stdout for both commands, routing categories, and invalid score rejection.
