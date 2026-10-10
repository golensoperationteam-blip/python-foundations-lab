# Exercise 13: Mocking and Unit-Test Patching

## Objective
Test network-dependent model integration without using the real internet.

## Concepts
- `unittest.mock.patch` replaces a dependency during a test.
- `urllib.request.Request` represents an HTTP request including method, headers, and body.
- Network failures can be handled at a service boundary with a predictable fallback.
- Mock responses make tests fast, deterministic, and safe for CI.
- Never put real credentials or production endpoints in exercise tests.

## Implementation
`query_remote_model_service(url, payload)` sends a JSON POST and expects a JSON object. `safe_model_call(url, prompt)` extracts response text and returns `Fallback Response` for connection or URL failures.

## Run
```bash
python -m pytest exercises/13_testing_mocking/test_solution.py
```

## Coverage
All network access is patched. Tests validate request serialization, successful response handling, and both URL and connection failures.
