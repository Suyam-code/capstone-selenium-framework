"""
Tier 2 - Assignment 4: JavaScript Alerts and Confirms
Site: https://the-internet.herokuapp.com/javascript_alerts
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_js_alert_confirm_prompt():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Alert -> accept
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        result = driver.find_element(By.ID, "result").text
        assert "successfully" in result.lower()

        # Confirm -> dismiss
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        driver.switch_to.alert.dismiss()
        result = driver.find_element(By.ID, "result").text
        assert "cancel" in result.lower()

        # Prompt -> type text, accept
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.send_keys("Automation")
        alert.accept()
        result = driver.find_element(By.ID, "result").text
        assert "Automation" in result

        print("PASSED: alert, confirm, and prompt all handled")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_js_alert_confirm_prompt()
