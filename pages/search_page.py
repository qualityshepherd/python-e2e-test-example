from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):
  url = '?search'
  searchbox = (By.CSS_SELECTOR, '#search_input')
  search_btn =    (By.CSS_SELECTOR, '[type="submit"]')
  results = (By.CSS_SELECTOR, '.search-result')
  no_results_msg = (By.CSS_SELECTOR, '#no-results')

  def __init__(self, driver):
    super(SearchPage, self).__init__(driver)

  def search_for(self, text):
    searchbox = self.element(self.searchbox)
    searchbox.clear()
    searchbox.send_keys(text)
    searchbox.send_keys(Keys.RETURN)

  def get_search_results_text(self):
    # results can take a second to display
    self.wait_for_element(self.results_displayed)
    return self.element(self.results_title).text