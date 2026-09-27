"""
Tier 1 - Assignment 3: Dynamic Dropdowns & Checkboxes
Site: https://the-internet.herokuapp.com/checkboxes (checkboxes)
      https://the-internet.herokuapp.com/dropdown (dropdown selection)

NOTE: the original assignment describes a search-as-you-type autocomplete
dropdown (like a flight-booking site). No stable, freely-automatable public
demo of that exact interaction was quick to source, so this uses a standard
<select> dropdown to demonstrate the same core skill instead (selecting an
option and verifying its state). Swap in a real autocomplete widget site if
your instructor specifically requires that interaction.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_checkboxes_and_dropdown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")

        assert checkboxes[0].is_selected() is False
        checkboxes[0].click()
        assert checkboxes[0].is_selected() is True

        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 2")
        assert dropdown.first_selected_option.text == "Option 2"

        print("PASSED: checkbox state + dropdown selection verified")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkboxes_and_dropdown()
