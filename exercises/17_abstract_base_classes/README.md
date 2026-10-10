# Exercise 17: Abstract Base Classes and Provider Interfaces

## Objective
Define a stable interface so application code can use interchangeable AI providers.

## Contract
BaseAIProvider declares abstract generate(prompt: str) -> str and get_model_info() -> dict methods. MockOpenAIProvider and MockAnthropicProvider implement both without network calls.

## Concepts
- Abstract base classes make incomplete implementations uninstantiable.
- A shared interface reduces coupling and makes providers replaceable.
- Mock implementations support deterministic tests without credentials or external services.

## Run
python -m pytest exercises/17_abstract_base_classes/test_solution.py
