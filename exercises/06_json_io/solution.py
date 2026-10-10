import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Union

JsonData = Union[Dict[str, Any], List[Any]]


def save_json(filepath: Union[str, Path], data: JsonData) -> bool:
    """
    Saves a dictionary or list to a JSON file with utf-8 encoding and 2-space indentation.
    Raises TypeError if data is not JSON serializable.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        serialized = json.dumps(data, indent=2)
    except (TypeError, OverflowError) as e:
        raise TypeError(f"Data is not JSON serializable: {e}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(serialized)
    return True


def load_json(filepath: Union[str, Path]) -> JsonData:
    """
    Loads and parses JSON data from a file.
    Raises FileNotFoundError if file does not exist.
    Raises ValueError if file content is not valid JSON.
    """
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted or invalid JSON in {path}: {e}")


if __name__ == "__main__":
    demo_file = Path("demo_agent_memory.json")
    sample_data = {
        "agent": "JARVIS",
        "version": "1.0.0",
        "capabilities": ["router", "search", "file_io"],
        "status": "ready"
    }
    save_json(demo_file, sample_data)
    loaded = load_json(demo_file)
    print(f"JSON I/O Successful: Agent '{loaded.get('agent')}' loaded with {len(loaded.get('capabilities', []))} capabilities.")
    if demo_file.exists():
        demo_file.unlink()
