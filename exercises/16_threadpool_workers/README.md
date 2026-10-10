# Exercise 16: ThreadPool Concurrency

## Objective
Run independent work items concurrently using concurrent.futures.ThreadPoolExecutor.

## Contract
parallel_process_tasks(tasks, max_workers=4) validates inputs, runs each task, and returns copied result dictionaries sorted by task_id (or id). By default, result is copied from value; an optional callable in run implements custom work. Callable exceptions propagate.

## Concepts
- Worker pools bound concurrently active threads.
- executor.map preserves input result correspondence; explicit sorting creates deterministic output.
- Threads suit I/O-bound work and usually do not accelerate CPU-bound Python bytecode under the GIL.
- Exceptions remain visible instead of being silently swallowed.

## Run
python -m pytest exercises/16_threadpool_workers/test_solution.py
