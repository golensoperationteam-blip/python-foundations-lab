import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location("exercise17_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
BaseAIProvider = _solution.BaseAIProvider
MockOpenAIProvider = _solution.MockOpenAIProvider
MockAnthropicProvider = _solution.MockAnthropicProvider


def test_abstract_provider_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseAIProvider()


@pytest.mark.parametrize("provider, name", [
    (MockOpenAIProvider(), "openai"),
    (MockAnthropicProvider(), "anthropic"),
])
def test_concrete_providers_satisfy_contract(provider, name):
    assert "hello" in provider.generate("hello")
    assert provider.get_model_info()["provider"] == name
    assert provider.get_model_info()["mock"] is True


def test_prompt_type_is_validated():
    with pytest.raises(TypeError):
        MockOpenAIProvider().generate(None)
