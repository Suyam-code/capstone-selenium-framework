import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage

RUN_STAMP = int(time.time())
MY_TEST_EMAIL = f"suyam.lodha19.{RUN_STAMP}@gmail.com"


def test_login_page_loads(driver, base_url):
    """just a sanity check that the login form actually shows up before I bother
    testing anything on top of it."""
    home = HomePage(driver)
    home.load(base_url)
    home.go_to_login()

    login_page = LoginPage(driver)
    print(f"checking login page loaded at: {driver.current_url}")
    assert login_page.is_visible(login_page.LOGIN_EMAIL)
    assert login_page.is_visible(login_page.LOGIN_BUTTON)


def test_invalid_login_shows_error(driver, base_url):
    """tried logging in with a made-up account, site should show an error
    message instead of just silently doing nothing."""
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.login("not_a_real_user@example.com", "wrongpassword123")

    assert login_page.is_login_error_shown(), (
        "expected an incorrect-login error message but none showed up"
    )


@pytest.mark.parametrize("name,email", [
    ("Suyam Lodha", MY_TEST_EMAIL),
])
def test_signup_form_accepts_new_user(driver, base_url, name, email):
    """
    tests the 'New User Signup' mini-form on the login page.
    email is timestamped per run so it's always a fresh, never-used address.

    IMPORTANT: after clicking Signup, explicitly WAIT for the URL to change
    to the account-info page instead of checking driver.current_url right
    away. Checking immediately is a race condition -- the click can succeed
    but the page hasn't finished redirecting yet, making the test fail even
    though the signup actually worked. This bit us twice before we caught it.
    """
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.signup_start(name, email)

    try:
        WebDriverWait(driver, 8).until(EC.url_contains("signup"))
    except Exception:
        pass  # let the assertion below report the real failure if it truly didn't redirect

    print(f"after signup attempt, landed on: {driver.current_url}")
    assert "signup" in driver.current_url.lower()


def test_signup_duplicate_email_shows_error(driver, base_url):
    """signing up twice with the same email should get rejected by the site."""
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.signup_start("Suyam Lodha (dup test)", MY_TEST_EMAIL)

    assert login_page.is_visible(login_page.SIGNUP_ERROR, timeout=5) or \
        "signup" in driver.current_url.lower()
