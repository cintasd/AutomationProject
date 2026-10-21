"""Runtime configuration for the SMEC browser automation project."""

import os


BASE_URL = os.getenv("BASE_URL", "https://devhub.mysmec.com/")
HEADLESS = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
