from base_page import BasePage
from selenium.webdriver.common.keys import Keys

class QsPage(BasePage):
    url = '' # same as base_url
    posts = 'div.post'
    searchbox = 'input#s';
    results = '.search-results';

    def __init__(self, driver):
        super(QsPage, self).__init__(driver)

    def get_num_posts(self):
        return len(self.elements(self.posts))

    def search_for(self, text):
        self.element(self.searchbox).send_keys(text)
        self.element(self.searchbox).send_keys(Keys.RETURN)
