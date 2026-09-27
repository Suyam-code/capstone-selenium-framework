import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from utils.csv_reader import read_csv

signup_cases = read_csv("signup_testdata.csv")


@pytest.mark.parametrize(
    "case",
    signup_cases,
    ids=[f"{row['name'] or 'blank-name'}_{row['email']}" for row in signup_cases],
)
def test_signup_validation(driver, base_url, case):
    """
    data-driven signup form validation, fed by data/signup_testdata.csv.

    for the row that EXPECTS success, the email gets a timestamp suffix so
    it's always fresh (never a duplicate). also explicitly waits for the
    url to change before checking it -- same race-condition fix as
    test_login.py, otherwise a slow redirect can look like a failure.
    """
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)

    expect_success = case["expect_success"].strip().lower() == "true"
    email = case["email"]

    if expect_success and "@" in email:
        local, domain = email.split("@", 1)
        email = f"{local}.{int(time.time())}@{domain}"

    login_page.signup_start(case["name"], email)

    if expect_success:
        try:
            WebDriverWait(driver, 8).until(EC.url_contains("signup"))
        except Exception:
            pass

    print(f"case: name='{case['name']}' email='{email}' -> landed on {driver.current_url}")
    proceeded_to_next_step = "signup" in driver.current_url.lower()

    if expect_success:
        assert proceeded_to_next_step, (
            f"expected signup to proceed for '{email}' but it didn't"
        )
    else:
        assert not proceeded_to_next_step, (
            f"expected signup to be rejected for name='{case['name']}' "
            f"email='{email}' but it proceeded anyway"
        )
