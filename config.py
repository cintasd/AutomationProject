"""Runtime configuration for the SMEC browser automation project."""

import os


BASE_URL = os.getenv("BASE_URL", "https://devhub.mysmec.com/")
BROWSER = os.getenv("BROWSER", "chromium").lower()
HEADLESS = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "15000"))
