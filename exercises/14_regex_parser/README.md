# Exercise 14: Regex and Structured Text Parsing

## Objective
Turn semi-structured model logs into typed records and redact API-style secrets before sharing logs.

## Concepts
- Named capture groups make regular expressions easier to maintain.
- `finditer` extracts repeated records from a larger log.
- Numeric captures should be converted to integers or floats for downstream analysis.
- Redaction should replace the full matched secret, not just part of it.
- Malformed records should be ignored rather than partially interpreted.

## Implementation
`extract_model_tags(log_text)` extracts model name, latency in milliseconds, and token count from tags such as `[MODEL: deepseek-r1 | LATENCY: 45ms | TOKENS: 120]`. `mask_sensitive_tokens(text)` redacts tokens matching `sk-[a-zA-Z0-9]{20,}`.

## Run
```bash
python -m pytest exercises/14_regex_parser/test_solution.py
```

## Coverage
Tests verify multiple tags, decimal latency, malformed input handling, matching-secret redaction, and preservation of nonmatching text.
