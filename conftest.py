import pytest
from selenium import webdriver


@pytest.fixture (autouse=True)
def driver_init():
    browser = webdriver.Chrome()
    browser.get('https://b2c.passport.rt.ru')

    yield browser
    browser.quit()