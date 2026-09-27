from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")

    def load(self, base_url):
        self.open(base_url)

    def go_to_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)
