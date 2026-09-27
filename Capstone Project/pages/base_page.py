from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import get_config


class BasePage:
    """
    every other page class inherits from this one. figured I'd rather write
    the wait/click/type logic once here than copy-paste it into every page.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, get_config()["explicit_wait"])

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        """
        this site runs Google ads that sometimes float over buttons and
        block normal clicks (hit this on the search button -- an ad iframe
        was literally sitting on top of it). normal .click() fails in that
        case with ElementClickInterceptedException, so if that happens,
        fall back to a JS click which bypasses the overlap check entirely.
        """
        el = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            el.click()
        except Exception:
            print(f"normal click failed for {locator}, falling back to JS click")
            self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def is_visible(self, locator, timeout=None):
        try:
            w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            w.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
