"""Capstone: an end-to-end autonomous mini-agent workflow."""
import argparse
import importlib.util
import json
import time
from pathlib import Path
from typing import Any


def _load_module(name: str, relative_path: str):
    path = Path(__file__).resolve().parents[1] / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load exercise module: {relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_task_module = _load_module("capstone_task_manager", "07_oop_task_manager/solution.py")
_timer_module = _load_module("capstone_timing", "08_decorators_and_retry/solution.py")
_regex_module = _load_module("capstone_regex", "14_regex_parser/solution.py")
_provider_module = _load_module("capstone_provider", "17_abstract_base_classes/solution.py")


class MiniAgentPipeline:
    """Manage tasks, redact secrets, call a mock provider, and report metrics."""

    def __init__(self, provider: Any | None = None) -> None:
        self.provider = provider or _provider_module.MockOpenAIProvider()
        self.tasks = _task_module.TaskManager()
        self._mask = _regex_module.mask_sensitive_tokens
        self._timed_generate = _timer_module.timed(self.provider.generate)

    def run(self, prompts: list[str]) -> dict[str, Any]:
        if not prompts:
            raise ValueError("at least one prompt is required")
        started = time.perf_counter()
        results, errors = [], []
        provider_seconds = 0.0
        for index, prompt in enumerate(prompts, start=1):
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append({"task_id": index, "error": "prompt must be a non-empty string"})
                continue
            try:
                task = _task_module.Task(
                    task_id=f"AGENT-{index:03d}",
                    title=f"Agent task {index}: {prompt[:60]}",
                )
                self.tasks.add_task(task)
                safe_prompt = self._mask(prompt)
                response, elapsed = self._timed_generate(safe_prompt)
                provider_seconds += elapsed
                task.mark_completed()
                results.append({
                    "task_id": index,
                    "task": task.title,
                    "prompt": safe_prompt,
                    "response": response,
                    "status": task.status,
                    "duration_seconds": round(elapsed, 6),
                })
            except Exception as exc:
                errors.append({"task_id": index, "error": f"{type(exc).__name__}: {exc}"})
        elapsed = time.perf_counter() - started
        return {
            "status": "completed" if not errors else ("partial" if results else "failed"),
            "results": results,
            "errors": errors,
            "summary": {
                "total": len(prompts),
                "completed": len(results),
                "failed": len(errors),
                "duration_seconds": round(elapsed, 6),
                "provider_duration_seconds": round(provider_seconds, 6),
                "provider": self.provider.get_model_info(),
            },
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the autonomous mini-agent capstone pipeline")
    parser.add_argument("--prompt", action="append", dest="prompts", help="prompt to process (repeatable)")
    args = parser.parse_args(argv)
    prompts = args.prompts or [
        "Summarize the model telemetry for this run.",
        "Check this API key sk-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234 and never reveal it.",
    ]
    report = MiniAgentPipeline().run(prompts)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] != "failed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
