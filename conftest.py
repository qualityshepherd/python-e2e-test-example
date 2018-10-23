import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('That\'s all folks!')
    driver.quit()