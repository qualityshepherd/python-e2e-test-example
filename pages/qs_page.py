from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from search_mod import Search


class QsPage(BasePage):
    url = '' # same as base_url)
    posts = (By.CSS_SELECTOR, 'div.post')
    results_displayed = (By.CSS_SELECTOR, '.search')
    results_title = (By.CSS_SELECTOR, '#content h2')
    no_results_msg = 'No posts found. Please try a different search.'
    # sidebar
    sidebar = (By.CSS_SELECTOR, '#sidebar')
    github_link = (By.CSS_SELECTOR, '#githubLink')

    def __init__(self, driver):
        super().__init__(driver)
        # include shared modules
        self.search = Search(driver)

    # get the number of posts
    def get_num_posts(self):
        return len(self.elements(self.posts))

    # get the text of search results title
    def get_search_results_text(self):
        # results can take a second to display
        self.wait_for_element(self.results_displayed)
        return self.element(self.results_title).text
