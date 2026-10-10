import functools
import time
from typing import Callable, Any, Tuple, Type


def timed(func: Callable[..., Any]) -> Callable[..., Tuple[Any, float]]:
    """
    Decorator that measures the execution duration of a function.
    Returns a tuple of (result, elapsed_seconds).
    Preserves original function name and docstring using functools.wraps.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        return result, elapsed

    return wrapper


def retry(
    max_attempts: int = 3,
    delay: float = 0.01,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """
    Decorator that retries a function upon encountering specified exceptions.
    Raises the last encountered exception if max_attempts is exceeded.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(delay)
            return None

        return wrapper

    return decorator


if __name__ == "__main__":
    @timed
    def simulated_agent_inference(tokens: int) -> str:
        time.sleep(0.05)
        return f"Generated {tokens} tokens"

    call_count = 0

    @retry(max_attempts=3, delay=0.01, exceptions=(ConnectionError,))
    def simulated_unstable_api_call() -> str:
        global call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError("Network timeout simulation")
        return "API Call Succeeded"

    res, duration = simulated_agent_inference(150)
    print(f"Timing Profiler: {res} in {duration:.4f}s")
    api_res = simulated_unstable_api_call()
    print(f"Retry Mechanism: {api_res} after {call_count} attempts.")
