import enum
import tomllib
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """log levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Environments(str, enum.Enum):
    """different environments that code runs on"""

    DEV = "development"
    PRODUCTION = "production"
    STAGING = "staging"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000

    workers_count: int = 1  # quantity of workers for uvicorn
    reload: bool = False  # Enable uvicorn reloading

    environment: str = Environments.DEV  # Current environment

    log_level: LogLevel = LogLevel.INFO

    sentry_dsn: Optional[str] = None
    sentry_sample_rate: float = 1.0

    # This variable is used to define
    # multiproc_dir. It's required for [uvi|guni]corn projects.
    prometheus_dir: Path = TEMP_DIR / "prom"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="CUSTOM_",
        env_file_encoding="utf-8",
    )

    @property
    def version(self) -> str:
        with open("pyproject.toml", "rb") as f:
            toml_data = tomllib.load(f)
        # Attempt to get the version from different possible locations
        version: str = toml_data.get("tool", {}).get("poetry", {}).get("version")
        return version


settings = Settings()
