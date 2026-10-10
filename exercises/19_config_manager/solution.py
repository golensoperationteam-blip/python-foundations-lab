"""Validated configuration with environment-variable overrides."""
import os
from typing import Any, Mapping


class ConfigManager:
    """Load defaults, apply environment overrides, and coerce values."""

    def __init__(
        self,
        defaults: Mapping[str, Any] | None = None,
        required_keys: tuple[str, ...] | list[str] = (),
        env_prefix: str = "APP_",
        environ: Mapping[str, str] | None = None,
    ) -> None:
        self._settings = dict(defaults or {})
        self._prefix = env_prefix
        source = os.environ if environ is None else environ
        for key in list(self._settings):
            env_key = f"{self._prefix}{key}".upper()
            if env_key in source:
                self._settings[key] = source[env_key]
        missing = [key for key in required_keys if key not in self._settings or self._settings[key] is None]
        if missing:
            raise ValueError(f"Missing required configuration keys: {', '.join(missing)}")

    def get_str(self, key: str, default: str | None = None) -> str:
        value = self._settings.get(key, default)
        if value is None:
            raise KeyError(key)
        return str(value)

    def get_int(self, key: str, default: int | None = None) -> int:
        value = self._settings.get(key, default)
        if value is None:
            raise KeyError(key)
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Configuration '{key}' must be an integer") from exc

    def get_bool(self, key: str, default: bool | None = None) -> bool:
        value = self._settings.get(key, default)
        if isinstance(value, bool):
            return value
        if value is None:
            raise KeyError(key)
        normalized = str(value).strip().lower()
        if normalized in {"1", "true", "yes", "on"}:
            return True
        if normalized in {"0", "false", "no", "off"}:
            return False
        raise ValueError(f"Configuration '{key}' must be a boolean")

    def as_dict(self) -> dict[str, Any]:
        return dict(self._settings)
