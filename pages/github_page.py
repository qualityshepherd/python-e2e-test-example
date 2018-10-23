from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GithubPage(BasePage):
    url = (By.CSS_SELECTOR, 'https://github.com/qualityshepherd')
    username = (By.CSS_SELECTOR, '.vcard-fullname')

    def __init__(self, driver):
        super().__init__(driver)

    # defines when the page is loaded
    def loaded(self):
        self.wait_for_element(self.username)