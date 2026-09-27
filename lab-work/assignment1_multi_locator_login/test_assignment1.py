"""
Tier 1 - Assignment 1: The Multi-Locator Challenge
Site: https://www.saucedemo.com/

Task: find username (By.ID), password (By.NAME), and login button (By.XPATH),
then assert the resulting URL contains /inventory.html.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_multi_locator_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.NAME, "password")
        login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url
        print("PASSED: reached", driver.current_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_multi_locator_login()
