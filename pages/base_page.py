"""Shared browser actions used by page objects."""

from typing import Optional

from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "") -> Optional[Response]:
        url = f"{self.base_url}/{path.lstrip('/')}" if path else f"{self.base_url}/"
        return self.page.goto(url, wait_until="domcontentloaded")

    @property
    def title(self) -> str:
        return self.page.title()
