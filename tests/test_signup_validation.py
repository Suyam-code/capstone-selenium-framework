import pytest

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
    covers: missing name, invalid email format, and (implicitly, from
    test_login.py) a valid case -- keeping this file focused on the
    REJECTION cases since the happy-path signup is already covered there
    with my real email.

    note: the "valid" row in the csv will only actually succeed the FIRST
    time it's ever run, since re-using the same email triggers the site's
    duplicate-email rejection instead. that's a known limitation of testing
    against a public demo site with no reset between runs -- documenting
    it here rather than pretending it's not a thing.
    """
    login_page = LoginPage(driver)
    login_page.open_login_page(base_url)
    login_page.signup_start(case["name"], case["email"])

    expect_success = case["expect_success"].strip().lower() == "true"
    print(f"case: name='{case['name']}' email='{case['email']}' -> landed on {driver.current_url}")

    proceeded_to_next_step = "signup" in driver.current_url.lower()

    if expect_success:
        assert proceeded_to_next_step, (
            f"expected signup to proceed for '{case['email']}' but it didn't"
        )
    else:
        assert not proceeded_to_next_step, (
            f"expected signup to be rejected for name='{case['name']}' "
            f"email='{case['email']}' but it proceeded anyway"
        )
