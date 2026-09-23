from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import get_config


def get_driver():
    """
    Builds and returns a configured Chrome WebDriver instance based on config.ini.
    Centralizing this means every test/fixture gets a browser the same way.
    """
    config = get_config()

    options = Options()
    if config["headless"]:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config["implicit_wait"])
    if not config["headless"]:
        driver.maximize_window()

    return driver
