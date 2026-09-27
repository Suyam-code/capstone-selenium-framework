import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")


def get_config():
    """
    Reads config/config.ini and returns a plain dict of settings.
    Keeps config access in one place so nothing else touches configparser directly.
    """
    parser = configparser.ConfigParser()
    parser.read(CONFIG_PATH)
    defaults = parser["DEFAULT"]

    return {
        "base_url": defaults.get("base_url"),
        "browser": defaults.get("browser", "chrome"),
        "implicit_wait": defaults.getint("implicit_wait", fallback=5),
        "explicit_wait": defaults.getint("explicit_wait", fallback=10),
        "headless": defaults.getboolean("headless", fallback=False),
    }
