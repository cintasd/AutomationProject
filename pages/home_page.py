"""Page object for the application's entry page."""

from typing import Optional

from playwright.sync_api import Response

from .base_page import BasePage


class HomePage(BasePage):
    def load(self) -> Optional[Response]:
        return self.open()
