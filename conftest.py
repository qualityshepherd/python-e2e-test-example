import pytest
import sys
from selenium import webdriver


# tell python where our modules are...
sys.path.append('pages')
sys.dont_write_bytecode = True

# add cli options...
def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://qualityshepherd.com', help='specify the base URL to test against')
    parser.addoption('--driver', action='store', default='chrome', help='chrome or firefox')

# driver fixture passed to all tests
@pytest.fixture(scope='session')
def driver(request):
    driver = request.config.getoption('--driver')
    if driver == 'firefox' or driver == 'ff':
        driver = webdriver.Firefox()
    elif driver == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError('invalid driver name: ' + driver)
    driver.set_window_size(1200, 800)
    driver.base_url = request.config.getoption('--url') or 'https://qualityshepherd.com/'
    yield driver
    driver.quit()