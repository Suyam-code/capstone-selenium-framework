"""
Tier 2 - Assignment 5: The HTML Web Table Extractor
Site: https://the-internet.herokuapp.com/tables
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_web_table_extractor():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/tables")
        rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

        target_last_name = "Doe"
        found_email = None

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            last_name = cells[0].text
            if last_name == target_last_name:
                found_email = cells[3].text
                break

        assert found_email is not None, f"couldn't find a row for {target_last_name}"
        print(f"PASSED: {target_last_name}'s email is {found_email}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_web_table_extractor()
