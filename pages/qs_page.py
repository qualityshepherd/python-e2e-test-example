from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class QsPage(BasePage):
  url = ''
  posts = (By.CSS_SELECTOR, 'div.post')
  post_titles = (By.CSS_SELECTOR, 'h2 a')
  github_link = (By.CSS_SELECTOR, '#github-social')
  older_entries_btn = (By.CSS_SELECTOR, '#pagination #next-btn')

  def __init__(self, driver):
    super(QsPage, self).__init__(driver)

  def get_num_posts(self):
    return len(self.elements(self.posts))

  def post_exists(self, post_title):
    titles = self.elements(self.post_titles)
    found = list(filter(lambda x: x.text == post_title, titles))
    return len(found) > 0

  def find_post_by_paging(self, post_title):
    ''' paginate back until we find a post by its title '''
    while not self.post_exists(post_title):
        self.element(self.older_entries_btn).click()
    return self.post_exists(post_title)