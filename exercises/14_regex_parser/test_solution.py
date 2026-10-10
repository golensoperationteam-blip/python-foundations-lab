import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("exercise14_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
extract_model_tags = _solution.extract_model_tags
mask_sensitive_tokens = _solution.mask_sensitive_tokens


def test_extracts_one_and_multiple_model_tags():
    logs = (
        "INFO request [MODEL: deepseek-r1 | LATENCY: 45ms | TOKENS: 120] done\n"
        "[MODEL: llama-3.3 | LATENCY: 12.5ms | TOKENS: 9]"
    )
    assert extract_model_tags(logs) == [
        {"model": "deepseek-r1", "latency_ms": 45, "tokens": 120},
        {"model": "llama-3.3", "latency_ms": 12.5, "tokens": 9},
    ]


def test_malformed_tags_are_ignored():
    assert extract_model_tags("[MODEL: x | LATENCY: slow | TOKENS: 4]") == []


def test_masks_matching_tokens_and_preserves_other_text():
    secret = "sk-" + "A1b2" * 6
    text = f"Authorization: {secret}; harmless=hello"
    assert mask_sensitive_tokens(text) == "Authorization: sk-***REDACTED***; harmless=hello"


def test_short_nonmatching_token_is_preserved():
    assert mask_sensitive_tokens("sk-short") == "sk-short"
