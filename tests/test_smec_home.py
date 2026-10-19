"""Basic availability check for the SMEC DevHub entry page."""

from config import BASE_URL
from pages.home_page import HomePage


def test_home_page_loads(page):
    home_page = HomePage(page, BASE_URL)

    response = home_page.load()

    assert response is not None, f"Navigation to {BASE_URL} did not return an HTTP response"
    assert response.status < 400, (
        f"Expected {BASE_URL} to load successfully, got HTTP {response.status}"
    )
    assert home_page.title.strip(), "The home page should have a non-empty document title"
