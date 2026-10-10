import asyncio
import sys
import time
from typing import List, Dict, Any

async def fetch_mock_model_response(model_id: str, prompt: str, delay: float = 0.05) -> Dict[str, Any]:
    """
    Simulates an asynchronous API request to an AI model provider.
    """
    await asyncio.sleep(delay)
    return {
        "model_id": model_id,
        "prompt": prompt,
        "status": "success",
        "tokens": len(prompt.split()) + 10,
        "latency": delay
    }

async def execute_parallel_queries(requests: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Executes multiple model inference queries concurrently using asyncio.gather.
    """
    tasks = [
        fetch_mock_model_response(req["model_id"], req["prompt"], req.get("delay", 0.05))
        for req in requests
    ]
    return await asyncio.gather(*tasks)

async def fetch_with_timeout(model_id: str, prompt: str, timeout: float, delay: float) -> Dict[str, Any]:
    """
    Executes a model call with a strict timeout guardrail.
    Raises TimeoutError if execution exceeds the timeout.
    """
    return await asyncio.wait_for(
        fetch_mock_model_response(model_id, prompt, delay),
        timeout=timeout
    )

def main():
    async def demo():
        queries = [
            {"model_id": "deepseek-r1", "prompt": "Solve math theorem", "delay": 0.04},
            {"model_id": "llama-3.3-70b", "prompt": "Code security audit", "delay": 0.03},
            {"model_id": "gemini-2.0-flash", "prompt": "Fast summary", "delay": 0.02}
        ]
        start = time.perf_counter()
        results = await execute_parallel_queries(queries)
        elapsed = time.perf_counter() - start

        print(f"--- AsyncIO Parallel Execution (50% Milestone) ---")
        print(f"Dispatched {len(results)} concurrent model queries in {elapsed:.4f}s.")
        for r in results:
            print(f"- [{r['model_id']}] latency: {r['latency']}s, tokens: {r['tokens']}")

    asyncio.run(demo())

if __name__ == "__main__":
    main()
