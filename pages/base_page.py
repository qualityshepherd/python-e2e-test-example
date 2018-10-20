
class BasePage(object) :
    base_url = 'https://qualityshepherd.com/'

    def __init__(self, driver):
        self.driver = driver
        # default wait for an element to be available in seconds
        driver.implicitly_wait(4)

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