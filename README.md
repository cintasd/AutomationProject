# SMEC DevHub UI automation

This project uses Python, Playwright, pytest, and the Page Object Model (POM).

## Project layout

```text
config.py               URL and browser settings
pages/base_page.py      Shared page actions
pages/home_page.py      DevHub entry page object
tests/conftest.py       Browser and page fixtures
tests/test_smec_home.py Basic entry page availability check
SMEC.py                 Convenience test runner
```

## Setup

Install dependencies in your project interpreter, then install the browser:

```bash
pip install -r requirements.txt
playwright install chromium
```

Run the starter check with either command:

```bash
pytest
python SMEC.py
```

The site defaults to `https://devhub.mysmec.com/`. Override settings with environment variables:

```bash
BASE_URL=https://devhub.mysmec.com/ BROWSER=chromium HEADLESS=false pytest
```

Supported `BROWSER` values are `chromium`, `firefox`, and `webkit`. Tests that require sign-in should use credentials supplied through environment variables or a local secrets file that is excluded from version control; do not commit credentials.

## Extending the POM

Add one page class per application page under `pages/`. Keep selectors and browser interactions in those page classes, and keep test scenarios and assertions under `tests/`. The public page could not be inspected during setup, so the initial check deliberately makes no assumptions about its login form or internal navigation.
