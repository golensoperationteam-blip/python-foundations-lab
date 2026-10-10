import subprocess
import sys
from pathlib import Path

SOLUTION = Path(__file__).with_name("solution.py")


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(SOLUTION), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_bench_subcommand_formats_record():
    result = run_cli("bench", "--model", "deepseek-r1", "--score", "92.5")
    assert result.returncode == 0
    assert "Benchmark: model=deepseek-r1, score=92.5/100" in result.stdout


def test_route_subcommand_resolves_coding():
    result = run_cli("route", "--task", "debug this Python function")
    assert result.returncode == 0
    assert "Route: coding" in result.stdout


def test_route_subcommand_resolves_language_and_general():
    language = run_cli("route", "--task", "summarize this report")
    general = run_cli("route", "--task", "forecast quarterly demand")
    assert language.returncode == 0 and "Route: language" in language.stdout
    assert general.returncode == 0 and "Route: general" in general.stdout


def test_invalid_benchmark_score_fails():
    result = run_cli("bench", "--model", "demo", "--score", "101")
    assert result.returncode != 0
