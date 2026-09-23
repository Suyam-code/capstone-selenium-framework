import os
import pytest

from utils.driver_factory import get_driver
from utils.config_reader import get_config

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")


@pytest.fixture
def driver():
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return get_config()["base_url"]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Runs after every test phase. If the 'call' phase fails, grab the
    driver from the test's fixtures and save a labelled screenshot.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            safe_name = item.name.replace("[", "_").replace("]", "").replace("/", "_")
            path = os.path.join(SCREENSHOT_DIR, f"{safe_name}.png")
            driver.save_screenshot(path)
