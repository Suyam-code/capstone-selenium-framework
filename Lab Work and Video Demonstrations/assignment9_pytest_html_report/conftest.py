import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.fixture
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            try:
                os.makedirs(SCREENSHOT_DIR, exist_ok=True)
                path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
                drv.save_screenshot(path)
            except Exception as e:
                print(f"couldn't save screenshot: {e}")
