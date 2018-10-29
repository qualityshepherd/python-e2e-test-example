from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


'''
Search is a shared object between multiple pages
'''
class Search(BasePage):
	searchbox = (By.CSS_SELECTOR, 'input#s')

	def for_text(self, text):
		''' search for the given text '''
		searchbox = self.element(self.searchbox)
		searchbox.clear()
		searchbox.send_keys(text)
		searchbox.send_keys(Keys.RETURN)