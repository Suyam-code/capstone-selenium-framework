from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    """product search on the /products page. this one gave me the most
    trouble out of everything -- see the comment in get_result_count()."""

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".features_items .productinfo p")

    def open_products_page(self, base_url):
        self.open(f"{base_url}/products")

    def search_for(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def has_results(self):
        return self.get_result_count() > 0

    def get_result_count(self):
        """
        NOTE TO SELF: originally used the shared find_all() helper here like
        everywhere else, but that broke on the "search for garbage, expect
        zero results" test case -- find_all() WAITS for elements to show up,
        so when there are correctly zero results, it just times out and
        throws an exception instead of returning 0.

        fix: don't wait for something that isn't supposed to exist. just give
        the page a second to settle after the search, then count directly.
        not the most elegant thing in the world but it works and honestly
        makes sense once you think about it -- you can't "wait" for absence.
        """
        import time
        time.sleep(1)
        count = len(self.driver.find_elements(*self.PRODUCT_CARDS))
        print(f"search returned {count} product card(s)")
        return count
