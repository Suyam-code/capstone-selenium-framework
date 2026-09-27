"""
Tier 2 - Assignment 6: Windows, Tabs, and Iframes
Site: https://the-internet.herokuapp.com/iframe (iframe)
      https://the-internet.herokuapp.com/windows (new tab)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


def test_windows_tabs_iframes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    try:
        # --- iframe ---
        driver.get("https://the-internet.herokuapp.com/iframe")
        driver.switch_to.frame("mce_0_ifr")
        body = driver.find_element(By.ID, "tinymce")
        body.clear()
        body.send_keys("Hello from automation")
        assert "Hello from automation" in body.text
        driver.switch_to.default_content()

        # --- windows/tabs ---
        driver.get("https://the-internet.herokuapp.com/windows")
        main_window = driver.current_window_handle
        driver.find_element(By.LINK_TEXT, "Click Here").click()

        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        new_window = [h for h in driver.window_handles if h != main_window][0]
        driver.switch_to.window(new_window)

        title = driver.title
        assert title == "New Window"
        driver.close()
        driver.switch_to.window(main_window)

        print("PASSED: iframe content set, new tab title verified:", title)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_windows_tabs_iframes()
