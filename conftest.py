from selenium.webdriver.common.by import By
import XPATH

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


o = Options()
o.add_experimental_option("detach", True)
o.add_experimental_option('excludeSwitches', ['enable-logging'])
o.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=o)


@pytest.fixture
def open_hello_window(request):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture()
def go_to_personal_account():
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()
    personal_account = driver.find_element(By.XPATH, XPATH.personal_account)
    personal_account.click()
