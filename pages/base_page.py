import time
from selenium.common.exceptions import NoSuchElementException

'''
base page class that is inherited by all pages and includes
things available to all pages
'''
class BasePage(object) :
    base_url = 'https://qualityshepherd.com/'

    def __init__(self, driver):
        self.driver = driver

    # wrapper for get()
    def goto(self, url):
        url = self.base_url + url
        self.driver.get(url)

    # get a single element
    def element(self, loc_str):
        return self.driver.find_element_by_css_selector(loc_str)

    # get multiple elements
    def elements(self, loc_str):
        return self.driver.find_elements_by_css_selector(loc_str)

    # should never need this... but...
    def sleep(self, seconds = 1):
        time.sleep(seconds)

    # test if an element exists
    def element_exits(self, element_css):
        try:
            self.element(element_css)
        except NoSuchElementException:
            return False
        return True
