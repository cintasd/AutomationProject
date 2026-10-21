# SMEC DevHub UI automation

This is a small browser-testing project for [SMEC DevHub](https://devhub.mysmec.com/).
It uses Python, Playwright, and pytest. Each test shows the browser steps directly:
start Playwright, open a page, check something, and close the browser.

## Project layout

```text
config.py               Website URL and headless setting
tests/test_smec_home.py Two beginner-friendly browser tests
SMEC.py                 Convenience test runner
```

## Setup

Use Python 3.9 or newer. From the project folder, install the Python dependencies
and the Playwright browser:

```bash
pip install -r requirements.txt
playwright install chromium
```

Run the tests with either command:

```bash
pytest
python SMEC.py
```

The tests check that the homepage responds successfully and displays its title and
main heading, and that **Start with Python** opens the Python course. Pytest shows
each `test_...` function separately in its test explorer.

## Configuration

The site defaults to `https://devhub.mysmec.com/`. Override settings with environment
variables when needed:

```bash
BASE_URL=https://devhub.mysmec.com/ BROWSER=chromium HEADLESS=false pytest
```

`HEADLESS=false` opens a visible Chromium window. By default, the tests run headless
so they work cleanly from pytest and the IDE test explorer. The browser closes when
each test finishes, so tests do not wait for keyboard input and can report their
results to pytest.

If navigation fails, pytest reports the configured URL and the browser's original
error. The test runs from your computer and network, so VPN or proxy settings can
affect whether the website is reachable. HTTP failures include the final URL and
status code.

## Running one test

In PyCharm, use the run icon beside a test function to run just that test. From a
terminal, include the test name:

```bash
pytest tests/test_smec_home.py::test_home_page_loads
```
