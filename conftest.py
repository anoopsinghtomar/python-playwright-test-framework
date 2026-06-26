import pytest
from playwright.sync_api import sync_playwright

from config.settings import Settings


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = getattr(p, Settings.BROWSER).launch(
            headless=Settings.HEADLESS
        )

        context = browser.new_context()

        page = context.new_page()

        yield page

        context.close()
        browser.close()