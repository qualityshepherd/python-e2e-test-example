from base_page import BasePage
from selenium.webdriver.common.keys import Keys

'''
Search is a shared object between multiple pages
'''
class Search(BasePage):
    searchbox = 'input#s';

    # search for the given text
    def for_text(self, text):
        searchbox = self.element(self.searchbox)
        searchbox.clear()
        searchbox.send_keys(text)
        searchbox.send_keys(Keys.RETURN)