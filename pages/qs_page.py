from base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from search_mod import Search

class QsPage(BasePage):
    url = '' # same as base_url
    posts = 'div.post'
    results = '.search-results';
    results_title = '#content h2'
    no_results_msg = 'No posts found. Please try a different search.'

    def __init__(self, driver):
        super().__init__(driver)
        # include shared modules
        self.search = Search(driver)

    # get the number of posts
    def get_num_posts(self):
        return len(self.elements(self.posts))

    # get the text of search results title
    def get_search_results_text(self):
        return self.element(self.results_title).text
