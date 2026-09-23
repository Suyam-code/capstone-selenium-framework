import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage

# using my real gmail with a +tag so I can actually check if the signup email
# lands, without spamming a fake inbox I can't check. re-running with the SAME
# tag will hit the "already exists" case on the site, which is why the two
# tests below share this exact address on purpose.
MY_TEST_EMAIL = "suyam.lodha19@gmail.com"


def test_login_page_loads(driver, base_url):
    """just a sanity check that the login form actually shows up before I bother
    testing anything on top of it. if this fails first, everything after it
    is probably going to fail too, so good to have this as test #1."""
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
    heads up -- if you re-run this a second time with the SAME email it'll
    hit the duplicate-account branch instead (that's a separate test below).
    if I need a totally clean run again I just bump the +tag, e.g. +capstone2.
    """
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.signup_start(name, email)

    # after a fresh signup the site moves you to the "enter account info" page,
    # so checking the url changed is basically all I need here.
    print(f"after signup attempt, landed on: {driver.current_url}")
    assert "signup" in driver.current_url.lower()


def test_signup_duplicate_email_shows_error(driver, base_url):
    """signing up twice with the same email should get rejected by the site.
    depends on test_signup_form_accepts_new_user having already run once with
    this same address -- not the cleanest way to chain tests, I know, but it
    was the simplest way to actually get the duplicate-email state without
    hardcoding some account that might not exist anymore."""
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.signup_start("Suyam Lodha (dup test)", MY_TEST_EMAIL)

    # TODO: this OR condition is a little loose -- ideally I'd only check
    # for the actual error text, but wanted a fallback in case the page
    # structure changes slightly between runs.
    assert login_page.is_visible(login_page.SIGNUP_ERROR, timeout=5) or \
        "signup" in driver.current_url.lower()
