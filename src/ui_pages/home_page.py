from playwright.sync_api import Page # Import the 'Page' type for type hinting, helps with autocompletion and static analysis

class HomePage:
    """
    Represents the Home Page of the DemoBlaze website.
    This is a Page Object, containing locators for elements and methods for actions on this page.
    """
    def __init__(self, page: Page):
        """
        Constructor for the HomePage Page Object.
        Args:
            page: The Playwright Page object, provided by the pytest-playwright fixture.
                  We store this 'page' object as an instance variable to interact with the browser.
        """
        self.page = page
        # Define locators for elements on the Home Page
        # We use page.locator() to define how to find elements on the page.
        # Playwright's locator API is powerful and recommended.

        self.login_link = page.locator("#login2") # Locator for the "Log in" link (using its ID)
        self.signup_link = page.locator("#signin2") # Locator for the "Sign up" link (using its ID)
        self.cart_link = page.locator("#cartur") # Locator for the "Cart" link (using its ID)
        self.home_link = page.locator(".nav-item a.nav-link[href='index.html']") # Locator for the "Home" link
        self.site_logo = page.locator("#nava") # Locator for the site logo/brand name (using its ID)

    def navigate(self):
        """
        Navigates the browser to the Home Page URL.
        """
        self.page.goto("https://www.demoblaze.com/") # Playwright's method to go to a URL

    def click_login(self):
        """
        Clicks on the "Log in" link.
        """
        self.login_link.click() # Playwright's method to click on the element located by self.login_link

    def click_signup(self):
        """
        Clicks on the "Sign up" link.
        """
        self.signup_link.click() # Playwright's method to click on the element located by self.signup_link

    def click_cart(self):
        """
        Clicks on the "Cart" link.
        """
        self.cart_link.click()

    def is_page_loaded(self) -> bool:
        """
        Verifies if the home page is loaded by checking for a key element's visibility.
        Returns:
            bool: True if the site logo is visible, indicating the page has loaded.
        """
        # Playwright's is_visible() method checks if the element is currently visible on the page.
        # This is a good way to assert that the page has rendered correctly.
        return self.site_logo.is_visible()

    def get_page_title(self) -> str:
        """
        Returns the title of the current page.
        """
        return self.page.title() # Playwright's method to get the page title