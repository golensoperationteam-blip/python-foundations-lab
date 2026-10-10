"""Provider interface contracts and deterministic mock implementations."""
from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response for a prompt."""

    @abstractmethod
    def get_model_info(self) -> dict:
        """Return provider and model metadata."""


class MockOpenAIProvider(BaseAIProvider):
    def generate(self, prompt: str) -> str:
        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string")
        return f"Mock OpenAI response: {prompt}"

    def get_model_info(self) -> dict:
        return {"provider": "openai", "model": "mock-gpt", "mock": True}


class MockAnthropicProvider(BaseAIProvider):
    def generate(self, prompt: str) -> str:
        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string")
        return f"Mock Anthropic response: {prompt}"

    def get_model_info(self) -> dict:
        return {"provider": "anthropic", "model": "mock-claude", "mock": True}
