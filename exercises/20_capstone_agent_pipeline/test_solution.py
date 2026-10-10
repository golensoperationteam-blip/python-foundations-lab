import importlib.util
import json
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location("exercise20_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
MiniAgentPipeline = _solution.MiniAgentPipeline


def test_end_to_end_pipeline_masks_secrets_and_reports_metrics():
    report = MiniAgentPipeline().run([
        "Summarize status",
        "Use key sk-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234 in a safe way",
    ])
    assert report["status"] == "completed"
    assert report["summary"]["total"] == 2
    assert report["summary"]["completed"] == 2
    assert report["summary"]["failed"] == 0
    assert report["summary"]["duration_seconds"] >= 0
    assert "sk-***REDACTED***" in report["results"][1]["prompt"]
    assert "sk-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234" not in report["results"][1]["prompt"]


def test_invalid_prompt_is_reported_without_aborting_batch():
    report = MiniAgentPipeline().run(["valid", "  "])
    assert report["status"] == "partial"
    assert report["summary"]["completed"] == 1
    assert report["summary"]["failed"] == 1


def test_provider_exception_is_reported_and_pipeline_continues():
    class FlakyProvider:
        def __init__(self):
            self.calls = 0
        def generate(self, prompt):
            self.calls += 1
            if self.calls == 1:
                raise RuntimeError("provider unavailable")
            return "recovered"
        def get_model_info(self):
            return {"provider": "test", "model": "flaky"}
    report = MiniAgentPipeline(FlakyProvider()).run(["first", "second"])
    assert report["status"] == "partial"
    assert report["summary"]["completed"] == 1
    assert report["summary"]["failed"] == 1
    assert report["results"][0]["response"] == "recovered"


def test_empty_batch_raises_and_cli_runs():
    with pytest.raises(ValueError, match="at least one"):
        MiniAgentPipeline().run([])
    import contextlib
    import io
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        assert _solution.main([]) == 0
    payload = json.loads(output.getvalue())
    assert payload["summary"]["total"] == 2
