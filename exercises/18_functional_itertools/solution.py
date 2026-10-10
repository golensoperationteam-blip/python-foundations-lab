"""Functional helpers for token usage and model-provider data."""
from functools import reduce
from itertools import chain, groupby
from typing import Iterable


def count_tokens(*token_batches: Iterable[str]) -> int:
    """Count tokens across iterable batches using itertools.chain."""
    return sum(1 for _ in chain.from_iterable(token_batches))


def group_models_by_provider(models: list[dict]) -> dict[str, list[dict]]:
    """Group copied model records by provider, regardless of input order."""
    ordered = sorted((dict(model) for model in models), key=lambda model: str(model.get("provider", "")))
    return {
        provider: list(group)
        for provider, group in groupby(ordered, key=lambda model: str(model.get("provider", "")))
    }


def running_token_consumption(consumptions: Iterable[int]) -> list[int]:
    """Return cumulative token totals using functools.reduce."""
    totals: list[int] = []
    reduce(lambda total, amount: (totals.append(total + amount) or total + amount), consumptions, 0)
    return totals
