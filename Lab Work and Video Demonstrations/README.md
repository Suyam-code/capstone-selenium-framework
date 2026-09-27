# Lab Work — Module 1 & Module 2 Assignments

Nine lab assignments from the course ToC (Tier 1 + Tier 2 Selenium
fundamentals, plus the Unit Test Frameworks / POM module), each in its
own folder with a working, runnable script.

## Setup (once)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Assignments

| # | Folder | Topic | Site Used |
|---|---|---|---|
| 1 | `assignment1_multi_locator_login` | Multi-locator login (ID/NAME/XPATH) | saucedemo.com |
| 2 | `assignment2_explicit_wait` | Explicit waits, no `time.sleep()` | the-internet.herokuapp.com |
| 3 | `assignment3_checkbox_dropdown` | Checkboxes + dropdown state | the-internet.herokuapp.com |
| 4 | `assignment4_js_alerts` | JS alert / confirm / prompt | the-internet.herokuapp.com |
| 5 | `assignment5_web_table` | Web table row/column extraction | the-internet.herokuapp.com |
| 6 | `assignment6_windows_tabs_iframes` | Iframes + new tab handling | the-internet.herokuapp.com |
| 7 | `assignment7_pom_restructure` | POM restructure of Assignment 1 | saucedemo.com |
| 8 | `assignment8_ddt` | Data-driven login from CSV | saucedemo.com |
| 9 | `assignment9_pytest_html_report` | PyTest fixtures + HTML report + screenshots | saucedemo.com |

## Running each one

Assignments 1–6 and 8 are standalone scripts:
```bash
cd assignment1_multi_locator_login
python test_assignment1.py
```

Assignment 7 needs to run from its own folder (for the `pages` import):
```bash
cd assignment7_pom_restructure
python test_assignment7.py
```

Assignment 9 uses PyTest with an HTML report:
```bash
cd assignment9_pytest_html_report
pytest test_assignment9.py --html=report.html --self-contained-html -v
```

## Notes
- Assignment 3's dropdown portion uses a standard `<select>` element rather
  than a true search-as-you-type autocomplete widget, since no stable public
  demo of that exact interaction was readily available — the checkbox state
  verification and dropdown selection still demonstrate the same core skill.
- All sites used (saucedemo.com, the-internet.herokuapp.com) are public,
  purpose-built QA practice sites — safe to automate freely.
