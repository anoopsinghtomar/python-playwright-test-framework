from playwright.sync_api import Locator


def wait_until_visible(locator: Locator):
    locator.wait_for(state="visible")


def wait_until_hidden(locator: Locator):
    locator.wait_for(state="hidden")