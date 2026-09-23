# Capstone: Selenium Automation Framework (PyTest + Unittest + POM)

## Objective
Build a maintainable Selenium WebDriver automation framework for
[automationexercise.com](https://automationexercise.com), covering login,
signup, and product search, using the Page Object Model, data-driven tests,
and HTML reporting.

## Tech Stack
- Python 3.x
- Selenium WebDriver 4
- PyTest (primary runner) + Unittest (secondary suite, per assignment spec)
- Page Object Model (POM)
- CSV-driven test data
- pytest-html reporting
- Screenshot-on-failure

## Project Structure
```
capstone-selenium-framework/
├── config/          # config.ini - base URL, browser, timeouts
├── data/            # CSV test data
├── pages/           # Page Object classes
├── tests/           # PyTest suite + conftest fixtures
├── legacy_unittest/ # Unittest suite (separate runner, same app)
├── reports/         # generated HTML reports
├── screenshots/     # failure screenshots
```

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Chrome must be installed. `webdriver-manager` handles the matching
ChromeDriver binary automatically — no manual driver download needed.

## Configuration
Edit `config/config.ini` to change the target site, browser, or timeouts:
```ini
[DEFAULT]
base_url = https://automationexercise.com
browser = chrome
implicit_wait = 5
explicit_wait = 10
headless = false
```

## Running the tests

**PyTest suite (with HTML report):**
```bash
pytest --html=reports/report.html --self-contained-html -v
```

**Unittest suite:**
```bash
python -m unittest legacy_unittest.test_login_unittest -v
```

**Run a single test file:**
```bash
pytest tests/test_product_search.py -v
```

## Test Data
- `data/search_testdata.csv` — search terms + expected result presence
- `data/signup_testdata.csv` — signup form validation cases

Edit these CSVs to add more scenarios without touching test code.

## Reporting & Screenshots
- HTML report is written to `reports/report.html` after each PyTest run.
- Any test that fails automatically saves a screenshot to `screenshots/`,
  named after the failing test (via a hook in `tests/conftest.py`).

## Design Notes
- All page interactions live in `pages/`, extending `BasePage`, which wraps
  Selenium's explicit waits — no `time.sleep()` anywhere in the suite.
- Locators use the site's `data-qa` attributes where available, since these
  are the most stable, automation-intended hooks the site exposes.
- The Unittest suite is kept in a separate `legacy_unittest/` folder rather
  than mixed into `tests/`, so PyTest's auto-discovery doesn't pick it up
  twice and the two frameworks stay clearly demonstrated as separate pieces.

## Author
Suyam Lodha — Capstone Project, Python Automation Course
