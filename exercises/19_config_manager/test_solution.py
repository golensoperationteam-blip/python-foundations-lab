import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location("exercise19_solution", Path(__file__).with_name("solution.py"))
_solution = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution)
ConfigManager = _solution.ConfigManager


def test_defaults_and_required_keys():
    config = ConfigManager({"host": "localhost", "port": 8000}, required_keys=("host",))
    assert config.get_str("host") == "localhost"
    assert config.get_int("port") == 8000
    with pytest.raises(ValueError, match="Missing required"):
        ConfigManager({"host": None}, required_keys=("host",))


def test_environment_overrides_and_typed_accessors():
    config = ConfigManager(
        {"host": "localhost", "port": 8000, "debug": False},
        env_prefix="APP_",
        environ={"APP_HOST": "api.example", "APP_PORT": "9000", "APP_DEBUG": "true"},
    )
    assert config.get_str("host") == "api.example"
    assert config.get_int("port") == 9000
    assert config.get_bool("debug") is True


@pytest.mark.parametrize("raw, expected", [
    ("true", True), ("yes", True), ("1", True),
    ("false", False), ("off", False), ("0", False),
])
def test_boolean_coercion(raw, expected):
    assert ConfigManager({"enabled": raw}).get_bool("enabled") is expected


def test_invalid_coercion_and_missing_keys_raise():
    config = ConfigManager({"port": "not-a-number", "flag": "sometimes"})
    with pytest.raises(ValueError, match="integer"):
        config.get_int("port")
    with pytest.raises(ValueError, match="boolean"):
        config.get_bool("flag")
    with pytest.raises(KeyError):
        config.get_str("missing")
