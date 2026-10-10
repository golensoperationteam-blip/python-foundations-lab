"""Validated and orderable model benchmark records."""
from dataclasses import asdict, dataclass
import json


@dataclass(order=True)
class ModelBenchmark:
    """A benchmark record ordered lexicographically by declared fields."""

    model_id: str
    score: float
    eval_date: str

    def __post_init__(self) -> None:
        if not 0 <= self.score <= 100:
            raise ValueError("score must be between 0 and 100 inclusive")

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)

    @classmethod
    def from_json(cls, json_str: str) -> "ModelBenchmark":
        data = json.loads(json_str)
        if not isinstance(data, dict):
            raise ValueError("JSON benchmark must be an object")
        try:
            return cls(
                model_id=data["model_id"],
                score=float(data["score"]),
                eval_date=data["eval_date"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("JSON must contain model_id, score, and eval_date") from exc
