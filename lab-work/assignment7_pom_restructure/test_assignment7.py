"""
Assignment 7: Page Object Model (POM) Restructure
Restructures Assignment 1's inline script into POM -- locators and UI
methods live in pages/login_page.py; test assertions stay here.

Run from THIS folder (assignment7_pom_restructure/) so the `pages` import
resolves correctly:
    python test_assignment7.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


def test_login_via_pom():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "/inventory.html" in driver.current_url
        print("PASSED via POM:", driver.current_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_via_pom()
