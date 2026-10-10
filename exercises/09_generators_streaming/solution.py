import sys
from typing import Generator, Iterable, List, Any, Callable

def stream_batches(iterable: Iterable[Any], batch_size: int = 10) -> Generator[List[Any], None, None]:
    """
    Memory-efficient generator that yields items from an iterable in batches of size batch_size.
    Raises ValueError if batch_size < 1.
    """
    if batch_size < 1:
        raise ValueError("batch_size must be >= 1")

    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

def filter_stream(stream: Iterable[Any], predicate: Callable[[Any], bool]) -> Generator[Any, None, None]:
    """
    Generator pipeline stage that yields only items satisfying the predicate function.
    """
    for item in stream:
        if predicate(item):
            yield item

def token_stream_simulator(text: str) -> Generator[str, None, None]:
    """
    Simulates streaming token generation from an LLM.
    """
    words = text.split()
    for word in words:
        yield word + " "

if __name__ == "__main__":
    sample_text = "Universal AI OS provides sovereign multi model routing and streaming verification"
    print("--- Simulating Streaming Tokens ---")
    tokens = list(token_stream_simulator(sample_text))
    print(f"Generated {len(tokens)} stream tokens: {''.join(tokens)}")

    data_range = range(1, 26)  # 25 numbers
    print("\n--- Batched Generator Stream (batch_size=10) ---")
    batches = list(stream_batches(data_range, batch_size=10))
    for i, b in enumerate(batches, 1):
        print(f"Batch {i}: {b}")

    evens = list(filter_stream(data_range, lambda x: x % 2 == 0))
    print(f"\nFiltered Evens Stream Count: {len(evens)}")
