import importlib.util
import subprocess
import sys
import types
import pytest
from pathlib import Path

solution_path = Path(__file__).parent / "solution.py"
spec = importlib.util.spec_from_file_location("solution_mod", solution_path)
solution_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_mod)

stream_batches = solution_mod.stream_batches
filter_stream = solution_mod.filter_stream
token_stream_simulator = solution_mod.token_stream_simulator

def test_stream_batches_is_generator():
    gen = stream_batches([1, 2, 3], batch_size=2)
    assert isinstance(gen, types.GeneratorType)
    result = list(gen)
    assert result == [[1, 2], [3]]

def test_stream_batches_exact_multiple():
    gen = stream_batches([1, 2, 3, 4], batch_size=2)
    assert list(gen) == [[1, 2], [3, 4]]

def test_stream_batches_empty_iterable():
    gen = stream_batches([], batch_size=5)
    assert list(gen) == []

def test_stream_batches_invalid_size():
    with pytest.raises(ValueError):
        list(stream_batches([1, 2], batch_size=0))

def test_filter_stream():
    numbers = [1, 2, 3, 4, 5, 6]
    evens_gen = filter_stream(numbers, lambda x: x % 2 == 0)
    assert isinstance(evens_gen, types.GeneratorType)
    assert list(evens_gen) == [2, 4, 6]

def test_token_stream_simulator():
    text = "Hello Sovereign AI World"
    tokens = list(token_stream_simulator(text))
    assert tokens == ["Hello ", "Sovereign ", "AI ", "World "]

def test_cli_execution():
    cmd = [sys.executable, str(solution_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "Simulating Streaming Tokens" in res.stdout
    assert "Batched Generator Stream" in res.stdout
    assert "Filtered Evens Stream Count: 12" in res.stdout
