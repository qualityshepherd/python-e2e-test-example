import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
base page class that is inherited by all pages and includes
things available to all pages
'''
class BasePage(object) :
    base_url = 'https://qualityshepherd.com/'
    timeout = {
        's': 1,
        'm': 3,
        'l': 6,
        'xl': 12
    }

    def __init__(self, driver):
        self.driver = driver

    # wrapper for get()
    def goto(self, url):
        url = self.base_url + url
        self.driver.get(url)

    # wait and get a single element via css selector (eg. #id)
    def element(self, loc_str):
        return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_element_by_css_selector(loc_str))

    # wait and get multiple elements via css selector (eg. .class)
    def elements(self, loc_str):
        return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_elements_by_css_selector(loc_str))

    def wait_for_element(self, loc_str):
        return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_element_by_css_selector(loc_str))

    # sleeps are an abomination... but...
    def sleep(self, seconds=1):
        time.sleep(seconds)

    # test if an element exists
    def element_exits(self, element_css):
        try:
            self.element(element_css)
        except NoSuchElementException:
            return False
        return True

    def switch_to_window(self, win_index):
        # this keeps chrome from hanging when switching windows... sadness
        self.sleep(1)
        print('switching to window:', win_index)
        self.driver.switch_to.window(self.driver.window_handles[win_index])