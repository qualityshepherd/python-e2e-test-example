import unittest
from selenium import webdriver
from qs_page import QsPage

class QualityShepherd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.qsPage = QsPage(self.driver)
        self.qsPage.goto(self.qsPage.url)

    # tests MUST start with `test_`
    def test_should_display_5_posts(self):
        assert self.qsPage.get_num_posts() is 5

    def test_should_return_search_results(self):
        self.qsPage.search_for('e2e')

        assert self.qsPage.element_exits(self.qsPage.results) is True

    def test_should_return_no_search_results_msg(self):
        self.qsPage.search_for('xxxxxxxx')

        assert self.qsPage.get_search_results_text() == self.qsPage.no_results_msg

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()