import pytest
from search_page import SearchPage

'''
autouse fixture sets up page objects and opens site and
function scope (default) ensures it runs for each test
'''
@pytest.fixture(scope="module", autouse=True)
def setup(driver):
  ''' makes pages available to all tests '''
  global SearchPage
  SearchPage = SearchPage(driver)
  SearchPage.goto(SearchPage.url)

def test_should_return_search_results(driver):
  SearchPage.search_for('python')

  assert SearchPage.element_exits(SearchPage.results) is True

def test_should_return_no_search_results_msg(driver):
  SearchPage.search_for('xxxxxxxx')

  assert SearchPage.element_exits(SearchPage.no_results_msg) is True
