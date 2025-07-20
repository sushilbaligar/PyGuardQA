# conftest.py
# This file is used by pytest to configure fixtures and plugins for the test suite.
import pytest
from playwright.sync_api import sync_playwright, Page # Import Page for type hinting
# Importing sync_playwright allows us to use Playwright in a synchronous context.
@pytest.fixture(scope="session") # 'session' scope means this fixture runs once per test session.
                                # Playwright usually uses 'function' scope for 'page' by default,
                                # which means a new page for each test. This is just an example
                                # if you wanted to customize how contexts are created for all tests.
def browser_context_args(browser_context_args):
    """
    This fixture is a hook provided by pytest-playwright.
    It allows you to modify the arguments passed to browser.new_context().
    We return the default arguments for now, but you could add things like:
    - viewport size: "viewport": {"width": 1920, "height": 1080}
    - locale: "locale": "en-GB"
    - permissions: "permissions": ["geolocation"]
    - ignore_https_errors: "ignore_https_errors": True
    """
    return {
        **browser_context_args, # Unpack default arguments provided by playwright plugin
        # Example of adding a custom setting (uncomment to activate)
        # "viewport": {"width": 1920, "height": 1080},
    }

# We might add custom user-defined fixtures here later if needed,
# e.g., for logging in, setting up test data, etc.