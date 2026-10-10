import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("exercise18_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
count_tokens = _solution.count_tokens
group_models_by_provider = _solution.group_models_by_provider
running_token_consumption = _solution.running_token_consumption


def test_token_count_chains_multiple_iterables():
    assert count_tokens(["a", "b"], ("c",), iter(["d", "e"])) == 5
    assert count_tokens() == 0


def test_models_group_even_when_input_unsorted():
    models = [
        {"name": "claude", "provider": "anthropic"},
        {"name": "gpt", "provider": "openai"},
        {"name": "other", "provider": "anthropic"},
    ]
    groups = group_models_by_provider(models)
    assert [m["name"] for m in groups["anthropic"]] == ["claude", "other"]
    assert groups["openai"][0]["name"] == "gpt"
    assert models[0]["name"] == "claude"


def test_running_consumption_uses_cumulative_totals():
    assert running_token_consumption([10, 4, 6]) == [10, 14, 20]
    assert running_token_consumption([]) == []
