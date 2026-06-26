"""
Base component containing reusable Playwright interaction methods.

All reusable UI components (Header, Sidebar, Modal, Table, etc.)
and BasePage inherit from this class.
"""

from pathlib import Path
from typing import Optional

from playwright.sync_api import Locator, Page, expect

from config.constants import DEFAULT_TIMEOUT, SCREENSHOTS_DIR
from utils.logger import get_logger


class BaseComponent:
    """
    Base class for all reusable UI components.
    """

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    # ------------------------------------------------------------------
    # Click Actions
    # ------------------------------------------------------------------

    def click(self, locator: Locator):
        """Click an element."""
        self.logger.info(f"Clicking: {locator}")
        locator.click()

    def double_click(self, locator: Locator):
        """Double-click an element."""
        self.logger.info(f"Double clicking: {locator}")
        locator.dblclick()

    def right_click(self, locator: Locator):
        """Right-click an element."""
        self.logger.info(f"Right clicking: {locator}")
        locator.click(button="right")

    # ------------------------------------------------------------------
    # Text Actions
    # ------------------------------------------------------------------

    def fill(self, locator: Locator, text: str):
        """Fill a text field."""
        self.logger.info(f"Entering text: {text}")
        locator.fill(text)

    def clear(self, locator: Locator):
        """Clear a text field."""
        locator.clear()

    def type(self, locator: Locator, text: str):
        """Type text character-by-character."""
        locator.press_sequentially(text)

    def press(self, locator: Locator, key: str):
        """Press a keyboard key."""
        locator.press(key)

    # ------------------------------------------------------------------
    # Mouse Actions
    # ------------------------------------------------------------------

    def hover(self, locator: Locator):
        locator.hover()

    def drag_and_drop(self, source: Locator, target: Locator):
        source.drag_to(target)

    # ------------------------------------------------------------------
    # Waits
    # ------------------------------------------------------------------

    def wait_for_visible(
        self,
        locator: Locator,
        timeout: Optional[int] = DEFAULT_TIMEOUT
    ):
        locator.wait_for(
            state="visible",
            timeout=timeout
        )

    def wait_for_hidden(
        self,
        locator: Locator,
        timeout: Optional[int] = DEFAULT_TIMEOUT
    ):
        locator.wait_for(
            state="hidden",
            timeout=timeout
        )

    # ------------------------------------------------------------------
    # Assertions
    # ------------------------------------------------------------------

    def should_be_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def should_be_hidden(self, locator: Locator):
        expect(locator).to_be_hidden()

    def should_have_text(self, locator: Locator, text: str):
        expect(locator).to_have_text(text)

    def should_contain_text(self, locator: Locator, text: str):
        expect(locator).to_contain_text(text)

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def get_text(self, locator: Locator) -> str:
        return locator.text_content() or ""

    def get_attribute(self, locator: Locator, attribute: str):
        return locator.get_attribute(attribute)

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def is_enabled(self, locator: Locator) -> bool:
        return locator.is_enabled()

    def count(self, locator: Locator) -> int:
        return locator.count()

    # ------------------------------------------------------------------
    # Screenshots
    # ------------------------------------------------------------------

    def take_screenshot(self, name: str):
        Path(SCREENSHOTS_DIR).mkdir(exist_ok=True)

        self.page.screenshot(
            path=f"{SCREENSHOTS_DIR}/{name}.png",
            full_page=True
        )