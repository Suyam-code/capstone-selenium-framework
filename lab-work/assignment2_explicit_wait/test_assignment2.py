"""
Tier 1 - Assignment 2: Synchronization & Explicit Waits
Site: https://the-internet.herokuapp.com/dynamic_loading/2

Constraint: no time.sleep() -- uses WebDriverWait + expected_conditions
to wait until the hidden text becomes visible after clicking Start.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_explicit_wait_dynamic_loading():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        finish_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        ).text

        assert finish_text == "Hello World!"
        print("PASSED:", finish_text)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_explicit_wait_dynamic_loading()
