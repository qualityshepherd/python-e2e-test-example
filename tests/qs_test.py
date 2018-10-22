import unittest
from selenium import webdriver
from qs_page import QsPage
from github_page import GithubPage

class QualityShepherd(unittest.TestCase):
    driver = webdriver.Firefox()
    qsPage = QsPage(driver)
    githubPage = GithubPage(driver)

    @classmethod # classmethods get called once per class as opposed to just using setUp
    def setUpClass(self):
        self.qsPage.goto(self.qsPage.url)

    # tests MUST start with `test_`
    def test_should_display_5_posts(self):
        assert self.qsPage.get_num_posts() is 5

    def test_should_return_search_results(self):
        self.qsPage.search.for_text('e2e')

        assert self.qsPage.element_exits(self.qsPage.results_displayed) is True

    def test_should_return_no_search_results_msg(self):
        self.qsPage.search.for_text('xxxxxxxx')

        assert 'No posts found' in self.qsPage.get_search_results_text()

    # TODO: this fails on chrome probably due to a bug in switch_to.window?
    def test_should_open_link_in_new_window(self):
        orig_win_index = 0
        self.qsPage.element(self.qsPage.github_link).click()
        # switch to new window
        new_win_index = 1
        self.qsPage.switch_to_window(new_win_index)

        assert self.githubPage.element_exits(self.githubPage.username) is True

        # cleanup...
        self.driver.close()
        self.qsPage.switch_to_window(orig_win_index)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()