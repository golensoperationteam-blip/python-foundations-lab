"""CLI demo for recording benchmarks and resolving task routes."""
import argparse


def resolve_route(task: str) -> str:
    normalized = task.strip().lower()
    if not normalized:
        raise ValueError("task must not be empty")
    if any(word in normalized for word in ("code", "debug", "program", "python")):
        return "coding"
    if any(word in normalized for word in ("summarize", "summary", "explain", "write")):
        return "language"
    if any(word in normalized for word in ("image", "vision", "picture")):
        return "vision"
    return "general"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Model benchmark and routing utility")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bench = subparsers.add_parser("bench", help="format a benchmark record")
    bench.add_argument("--model", required=True, help="model identifier")
    bench.add_argument("--score", required=True, type=float, help="score from 0 to 100")

    route = subparsers.add_parser("route", help="resolve a task routing category")
    route.add_argument("--task", required=True, help="natural-language task description")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "bench":
        if not 0 <= args.score <= 100:
            parser.error("--score must be between 0 and 100")
        print(f"Benchmark: model={args.model}, score={args.score:g}/100")
    elif args.command == "route":
        try:
            category = resolve_route(args.task)
        except ValueError as exc:
            parser.error(str(exc))
        print(f"Route: {category}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
