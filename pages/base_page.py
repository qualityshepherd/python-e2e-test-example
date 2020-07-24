import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
base page class that is inherited by all pages and includes
things available to all pages
'''
class BasePage() :
  timeout = {
    's': 1,
    'm': 3,
    'l': 6,
    'xl': 12
  }

  '''constructor'''
  def __init__(self, driver):
    self.driver = driver
    self.base_url = driver.base_url

  def goto(self, url):
    ''' wrapper for get() '''
    url = self.base_url + url
    self.driver.get(url)
    return url

  def get_base_url(self):
    return self.base_url

  def element(self, locator):
    ''' wait and get a single element via css selector (eg. #id) '''
    return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_element(*locator))

  def elements(self, locator):
    ''' wait and get multiple elements via css selector (eg. .class) '''
    return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_elements(*locator))

  def wait_for_element(self, locator):
    return WebDriverWait(self.driver, self.timeout['l']).until(lambda x: x.find_element(*locator))

  def sleep(self, seconds=1):
    ''' sleeps are an abomination... but... '''
    time.sleep(seconds)

  def element_exits(self, element_css):
    ''' test if an element exists '''
    try:
        self.element(element_css)
    except NoSuchElementException:
        return False
    return True

  def switch_to_new_window(self):
    # this keeps chrome from hanging when switching windows... sadness
    self.sleep(1)
    windows = self.driver.window_handles
    self.driver.switch_to.window(windows[-1])

  def switch_to_first_window(self):
    windows = self.driver.window_handles
    # close current window
    self.driver.close()
    self.driver.switch_to.window(windows[0])