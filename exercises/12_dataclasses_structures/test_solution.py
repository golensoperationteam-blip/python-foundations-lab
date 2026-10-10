import importlib.util
import json
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location("exercise12_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
ModelBenchmark = _solution.ModelBenchmark


def test_dataclass_sorting_uses_score_key():
    records = [
        ModelBenchmark("model-a", 91.0, "2026-01-01"),
        ModelBenchmark("model-b", 72.5, "2026-01-02"),
        ModelBenchmark("model-c", 84.0, "2026-01-03"),
    ]
    assert [item.score for item in sorted(records, key=lambda item: item.score)] == [72.5, 84.0, 91.0]
    # order=True follows declared field order, so score-only ranking uses an explicit key.
    assert sorted(records)[0].model_id == "model-a"


@pytest.mark.parametrize("score", [-0.01, 100.01])
def test_invalid_scores_raise_value_error(score):
    with pytest.raises(ValueError, match="score must be between"):
        ModelBenchmark("test-model", score, "2026-01-01")


@pytest.mark.parametrize("score", [0, 50.5, 100])
def test_json_roundtrip(score):
    record = ModelBenchmark("deepseek-r1", score, "2026-10-10")
    encoded = record.to_json()
    assert json.loads(encoded)["model_id"] == "deepseek-r1"
    assert ModelBenchmark.from_json(encoded) == record
