"""Mockable remote model service helpers."""
import json
from urllib.error import URLError
from urllib.request import Request, urlopen


def query_remote_model_service(url: str, payload: dict) -> dict:
    """POST JSON to a remote endpoint and return its decoded JSON object."""
    body = json.dumps(payload).encode("utf-8")
    request = Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=10) as response:
        decoded = json.loads(response.read().decode("utf-8"))
    if not isinstance(decoded, dict):
        raise ValueError("Remote model service must return a JSON object")
    return decoded


def safe_model_call(url: str, prompt: str) -> str:
    """Call the model service and return its response text or a safe fallback."""
    try:
        result = query_remote_model_service(url, {"prompt": prompt})
        text = result.get("response", result.get("text", ""))
        return text if isinstance(text, str) and text.strip() else "Fallback Response"
    except (ConnectionError, URLError):
        return "Fallback Response"
