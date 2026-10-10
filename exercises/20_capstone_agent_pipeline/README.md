# Exercise 20: Capstone — Autonomous Mini Agent Pipeline

## Goal
Combine task management, execution timing, regex-based secret masking, and a mock provider into one end-to-end workflow.

## Architecture
1. Task management: each valid prompt becomes a task in the existing TaskManager.
2. Input hygiene: API-style secrets are redacted before provider execution.
3. Provider abstraction: a provider implementing generate and get_model_info executes each prompt; the default is a mock provider.
4. Resilience: invalid prompts and provider exceptions are recorded per task, and later tasks continue.
5. Observability: JSON output includes completed/failed counts, elapsed duration, and provider metadata.

The capstone dynamically loads earlier exercise modules by file path because exercise directory names begin with digits. No external API or credential is required.

## Run
python exercises/20_capstone_agent_pipeline/solution.py
python exercises/20_capstone_agent_pipeline/solution.py --prompt "Summarize deployment status"
python -m pytest exercises/20_capstone_agent_pipeline/test_solution.py
python -m pytest

## Output contract
The CLI prints a JSON object with status, results, errors, and summary. Status is completed, partial, or failed; the process returns non-zero only when all tasks fail.

## Security note
Secret masking is a lightweight demonstration, not a substitute for a dedicated secrets scanner. Never send production secrets to a model provider.
