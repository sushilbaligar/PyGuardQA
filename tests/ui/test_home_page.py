import pytest
from playwright.sync_api import Page # Import 'Page' for type hinting (helps our IDE and clarity)
from src.ui_pages.home_page import HomePage # Import our HomePage Page Object

# Pytest automatically discovers functions starting with 'test_'.
# The 'page: Page' parameter tells Pytest to inject the Playwright Page object.
# Playwright's pytest plugin handles launching the browser, creating a context and page,
# and passing it to this test function.

def test_home_page_navigation_and_title(page: Page):
    """
    Tests if the home page navigates correctly and has the expected title.
    """
    # 1. Instantiate the HomePage Page Object
    # We pass the 'page' fixture (the browser page) to our Page Object.
    home_page = HomePage(page)

    # 2. Perform actions using the Page Object's methods
    home_page.navigate() # Go to the home page URL defined in HomePage

    # 3. Assertions (verify the outcome)
    # Pytest uses Python's standard 'assert' keyword for verification.
    assert home_page.is_page_loaded(), "Home page logo should be visible, indicating page loaded"
    assert "STORE" in home_page.get_page_title(), "Page title should contain 'STORE'"
    print(f"DEBUG: Page title is: '{home_page.get_page_title()}'") # Add a debug print for visibility

def test_home_page_links_visibility(page: Page):
    """
    Tests if key links like "Log in" and "Sign up" are visible on the home page.
    """
    home_page = HomePage(page)
    home_page.navigate() # Ensure we are on the home page

    # Playwright's locators have methods like .wait_for() and .is_visible().
    # .wait_for(state="visible") makes sure the element is actually displayed on the page
    # before we try to assert its visibility. This helps with dynamic loading.
    home_page.login_link.wait_for(state="visible")
    home_page.signup_link.wait_for(state="visible")
    home_page.cart_link.wait_for(state="visible")

    # Assert that the elements are visible
    assert home_page.login_link.is_visible(), "Login link should be visible"
    assert home_page.signup_link.is_visible(), "Sign up link should be visible"
    assert home_page.cart_link.is_visible(), "Cart link should be visible"

    print("DEBUG: All key links verified to be visible.")