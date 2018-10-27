import pytest
from qs_page import QsPage
from github_page import GithubPage


# autouse fixture sets up page objects and opens site
@pytest.fixture(autouse=True)
def setup(driver):
    # makes pages available to all tests
    global qsPage, githubPage
    qsPage = QsPage(driver)
    githubPage = GithubPage(driver)
    qsPage.goto(qsPage.url)

# tests MUST start with `test_` to run with pytest
def test_should_display_5_posts(driver):
    assert qsPage.get_num_posts() is 5

def test_should_return_search_results(driver):
    qsPage.search.for_text('e2e')

    assert qsPage.element_exits(qsPage.results_displayed) is True

def test_should_return_no_search_results_msg(driver):
    qsPage.search.for_text('xxxxxxxx')

    assert 'No posts found' in qsPage.get_search_results_text()

def test_should_open_link_in_new_window(driver):
    orig_win_index = 0
    qsPage.element(qsPage.github_link).click()
    # switch to new window
    new_win_index = 1
    githubPage.switch_to_window(new_win_index)

    assert githubPage.element_exits(githubPage.username) is True

    # cleanup...
    driver.close()
    qsPage.switch_to_window(orig_win_index)

def test_sidebar_has_a_set_width(driver):
    assert qsPage.element(qsPage.sidebar).size['width'] == 280
