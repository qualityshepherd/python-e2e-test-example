from base_page import BasePage

class GithubPage(BasePage):
    url = 'https://github.com/qualityshepherd';
    username = '.vcard-fullname'

    def __init__(self, driver):
        super().__init__(driver)