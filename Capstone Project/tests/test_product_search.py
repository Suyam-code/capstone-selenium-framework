import pytest

from pages.search_page import SearchPage
from utils.csv_reader import read_csv

search_cases = read_csv("search_testdata.csv")


@pytest.mark.parametrize(
    "case",
    search_cases,
    ids=[row["search_term"] for row in search_cases],
)
def test_product_search(driver, base_url, case):
    """
    Data-driven search test: reads data/search_testdata.csv and asserts
    result presence/absence matches the expected outcome per row.
    """
    search_page = SearchPage(driver)
    search_page.open_products_page(base_url)
    search_page.search_for(case["search_term"])

    expect_results = case["expect_results"].strip().lower() == "true"
    has_results = search_page.has_results()

    if expect_results:
        assert has_results, f"Expected results for '{case['search_term']}' but got none"
    else:
        assert not has_results, f"Expected no results for '{case['search_term']}' but got some"
