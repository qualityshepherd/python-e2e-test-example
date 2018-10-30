from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from search_mod import Search


class QsPage(BasePage):
    url = '' # same as base_url)
    posts = (By.CSS_SELECTOR, 'div.post')
    post_titles = (By.CSS_SELECTOR, 'h2 a')
    results_displayed = (By.CSS_SELECTOR, '.search')
    results_title = (By.CSS_SELECTOR, '#content h2')
    no_results_msg = 'No posts found. Please try a different search.'
    # sidebar
    sidebar = (By.CSS_SELECTOR, '#sidebar')
    github_link = (By.CSS_SELECTOR, '#githubLink')
    # older btn is on left; newer btn on right
    older_entries_btn = (By.CSS_SELECTOR, '.navigation .alignleft a')

    def __init__(self, driver):
        super(QsPage, self).__init__(driver)
        # include shared modules
        self.search = Search(driver)

    def get_num_posts(self):
        ''' get the number of posts '''
        return len(self.elements(self.posts))

    def get_search_results_text(self):
        ''' get the text of search results title '''
        # results can take a second to display
        self.wait_for_element(self.results_displayed)
        return self.element(self.results_title).text

    def post_exists(self, post_title):
        ''' test if a post exists '''
        titles = self.elements(self.post_titles)
        found = list(filter(lambda x: x.text == post_title, titles))
        return len(found) > 0

    def find_post_by_paging(self, post_title):
        ''' paginate back until we find a post by its title '''
        while not self.post_exists(post_title):
            self.element(self.older_entries_btn).click()
        return self.post_exists(post_title)