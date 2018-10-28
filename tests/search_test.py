import pytest
from qs_page import QsPage

'''
autouse fixture sets up page objects and opens site and 
function scope (default) ensures it runs for each test
'''
@pytest.fixture(autouse=True)
def setup(driver):
    # makes pages available to all tests
    global qsPage
    qsPage = QsPage(driver)
    qsPage.goto(qsPage.url)

def test_should_return_search_results(driver):
    qsPage.search.for_text('e2e')

    assert qsPage.element_exits(qsPage.results_displayed) is True

def test_should_return_no_search_results_msg(driver):
    qsPage.search.for_text('xxxxxxxx')

    assert 'No posts found' in qsPage.get_search_results_text()