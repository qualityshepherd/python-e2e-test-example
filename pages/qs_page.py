from base_page import BasePage

class QsPage(BasePage):
    url = '' # same as base_url
    posts = 'div.post'

    def __init__(self, driver):
        super(QsPage, self).__init__(driver)

    def getNumPosts(self):
        return len(self.elements(self.posts))