# Exercise 19: Dynamic Configuration and Settings Manager

## Objective
Combine safe defaults with environment-specific overrides and typed accessors.

## Behavior
ConfigManager copies defaults, overrides matching keys using uppercase environment names such as APP_PORT, and validates required settings. get_str, get_int, and get_bool perform explicit coercion and raise useful errors for missing or malformed values. Passing environ makes tests deterministic.

## Concepts
- Environment variables are strings and need validation before use.
- Defaults keep local development simple; required-key checks catch incomplete deployments.
- Avoid logging secrets and avoid mutating the caller's defaults dictionary.

## Run
python -m pytest exercises/19_config_manager/test_solution.py
