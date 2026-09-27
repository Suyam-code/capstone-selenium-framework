"""
Assignment 8: Data-Driven Automation (DDT)
Reads multiple login test cases from an external CSV file and loops
through them, asserting correct success/failure for each combination.

Run from THIS folder:
    python test_assignment8.py
"""
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def read_login_cases():
    path = os.path.join(os.path.dirname(__file__), "data", "login_data.csv")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_ddt_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        for case in read_login_cases():
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys(case["username"])
            driver.find_element(By.ID, "password").send_keys(case["password"])
            driver.find_element(By.ID, "login-button").click()

            expect_success = case["expect_success"].strip().lower() == "true"
            logged_in = "/inventory.html" in driver.current_url

            if expect_success:
                assert logged_in, f"expected success for {case['username']}"
            else:
                assert not logged_in, f"expected failure for {case['username']}"

            print(f"case {case['username']}/{case['password']} -> "
                  f"success={logged_in} (expected={expect_success})")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_ddt_login()
