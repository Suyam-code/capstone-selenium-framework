from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    the /login page on automationexercise.com is a bit weird -- it's actually
    TWO forms stacked on one page: an existing-user login form and a new-user
    signup form. took me a minute of inspecting the page to realize that.

    used the data-qa attributes for locators since this site actually built
    those in specifically for automation (nice change from guessing at
    auto-generated ids/classes like most sites give you).
    """

    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'incorrect')]")

    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SIGNUP_ERROR = (By.XPATH, "//p[contains(text(),'Email Address already exist')]")

    LOGGED_IN_INDICATOR = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def open_login_page(self, base_url):
        self.open(f"{base_url}/login")

    def login(self, email, password):
        self.type(self.LOGIN_EMAIL, email)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def signup_start(self, name, email):
        """this only fills the little name+email box that kicks off signup --
        the site then takes you to a second page with address/password/etc,
        which I'm not automating for now since it's not needed for what
        the capstone is testing. maybe later if I have time."""
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def is_login_error_shown(self):
        return self.is_visible(self.LOGIN_ERROR, timeout=5)

    def is_logged_in(self):
        return self.is_visible(self.LOGGED_IN_INDICATOR, timeout=5)
