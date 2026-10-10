"""Extract structured model telemetry and redact API tokens."""
import re

_MODEL_LOG = re.compile(
    r"\[\s*MODEL:\s*(?P<model>[^|\]]+?)\s*\|\s*LATENCY:\s*(?P<latency>\d+(?:\.\d+)?)\s*ms\s*\|\s*TOKENS:\s*(?P<tokens>\d+)\s*\]"
)
_SECRET = re.compile(r"sk-[a-zA-Z0-9]{20,}")


def extract_model_tags(log_text: str) -> list[dict]:
    """Parse all well-formed model telemetry tags from a log string."""
    records = []
    for match in _MODEL_LOG.finditer(log_text):
        latency = float(match.group("latency"))
        records.append({
            "model": match.group("model").strip(),
            "latency_ms": int(latency) if latency.is_integer() else latency,
            "tokens": int(match.group("tokens")),
        })
    return records


def mask_sensitive_tokens(text: str) -> str:
    """Replace token-like secrets without exposing any matched characters."""
    return _SECRET.sub("sk-***REDACTED***", text)
