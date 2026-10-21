"""Basic smoke tests for the SMEC DevHub homepage."""

from playwright.sync_api import sync_playwright

from config import BASE_URL, HEADLESS


def test_home_page_loads():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        try:
            page = browser.new_page()
            response = page.goto(BASE_URL)

            assert response is not None, f"Navigation to {BASE_URL} did not return an HTTP response"
            assert response.status < 400, (
                f"Expected {BASE_URL} to load successfully, but received HTTP {response.status}. "
                f"Final URL: {page.url}"
            )
            assert "Learn to code without getting stuck" in page.title()
            assert page.get_by_role("heading", level=1).inner_text().strip() == (
                "Learn to code without getting stuck."
            )
        finally:
            browser.close()


def test_start_python_link_opens_python_course():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        try:
            page = browser.new_page()
            page.goto(BASE_URL)

            page.get_by_role("link", name="Start with Python").first.click()
            page.wait_for_url("**/python")

            assert page.url.rstrip("/").endswith("/python")
        finally:
            browser.close()
