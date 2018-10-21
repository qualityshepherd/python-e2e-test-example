from base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class QsPage(BasePage):
    url = '' # same as base_url
    posts = 'div.post'
    searchbox = 'input#s';
    results = '.search-results';
    results_title = '#content h2'
    no_results_msg = 'No posts found. Please try a different search.'

    def __init__(self, driver):
        super(QsPage, self).__init__(driver)

    def get_num_posts(self):
        return len(self.elements(self.posts))

    def search_for(self, text):
        self.element(self.searchbox).send_keys(text)
        self.element(self.searchbox).send_keys(Keys.RETURN)

    def get_search_results_text(self):
        return self.element(self.results_title).text
