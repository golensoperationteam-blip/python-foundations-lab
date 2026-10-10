import importlib.util
import json
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.error import URLError

_spec = importlib.util.spec_from_file_location("exercise13_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
query_remote_model_service = _solution.query_remote_model_service
safe_model_call = _solution.safe_model_call


def test_query_remote_service_posts_json_and_decodes_response():
    response = MagicMock()
    response.__enter__.return_value = response
    response.read.return_value = json.dumps({"response": "Hello from mock"}).encode()
    with patch.object(_solution, "urlopen", return_value=response) as mocked:
        result = query_remote_model_service("https://example.invalid/model", {"prompt": "hello"})
    assert result == {"response": "Hello from mock"}
    request = mocked.call_args.args[0]
    assert request.get_method() == "POST"
    assert json.loads(request.data.decode()) == {"prompt": "hello"}


def test_safe_model_call_returns_remote_response():
    with patch.object(_solution, "query_remote_model_service", return_value={"response": "Model says hi"}):
        assert safe_model_call("https://example.invalid/model", "hello") == "Model says hi"


def test_safe_model_call_falls_back_on_network_failure():
    with patch.object(_solution, "query_remote_model_service", side_effect=URLError("offline")):
        assert safe_model_call("https://example.invalid/model", "hello") == "Fallback Response"


def test_safe_model_call_falls_back_on_connection_error():
    with patch.object(_solution, "query_remote_model_service", side_effect=ConnectionError("offline")):
        assert safe_model_call("https://example.invalid/model", "hello") == "Fallback Response"
