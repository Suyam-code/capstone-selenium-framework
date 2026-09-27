"""
Assignment 9: PyTest Integration with HTML Reporting
Uses a PyTest fixture (in conftest.py) for driver init/teardown, and
generates an HTML report with a screenshot embedded for any failure.

Run from THIS folder:
    pytest test_assignment9.py --html=report.html --self-contained-html -v
"""
from selenium.webdriver.common.by import By


def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url


def test_invalid_login_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in error.lower()
