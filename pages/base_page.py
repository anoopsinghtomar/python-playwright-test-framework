from playwright.sync_api import Page

from components.base_component import BaseComponent


class BasePage(BaseComponent):
    """
    Base class for all application pages.

    Inherits all common UI interaction methods from BaseComponent and
    provides page-level operations such as navigation and page state.
    """

    def __init__(self, page: Page):
        super().__init__(page)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def open(self, url: str):
        """Navigate to a URL."""
        self.logger.info(f"Opening URL: {url}")
        self.page.goto(url)

    def refresh(self):
        """Refresh the current page."""
        self.logger.info("Refreshing page")
        self.page.reload()

    def go_back(self):
        """Navigate to the previous page."""
        self.logger.info("Navigating back")
        self.page.go_back()

    def go_forward(self):
        """Navigate to the next page."""
        self.logger.info("Navigating forward")
        self.page.go_forward()

    # ------------------------------------------------------------------
    # Page Information
    # ------------------------------------------------------------------

    def current_url(self) -> str:
        """Return the current page URL."""
        return self.page.url

    def title(self) -> str:
        """Return the current page title."""
        return self.page.title()

    # ------------------------------------------------------------------
    # Page Waits
    # ------------------------------------------------------------------

    def wait_for_page_load(self):
        """Wait until the page reaches the network idle state."""
        self.logger.info("Waiting for page to fully load")
        self.page.wait_for_load_state("networkidle")