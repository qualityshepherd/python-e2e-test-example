import unittest
from selenium import webdriver
from qs_page import QsPage

class QualityShepherd(unittest.TestCase):
    driver = webdriver.Chrome()
    qsPage = QsPage(driver)

    def setUp(self):
        self.qsPage.goto(self.qsPage.url)

        # tests MUST start with `test_`
    def test_should_display_5_posts(self):
        assert self.qsPage.getNumPosts() is 5

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()