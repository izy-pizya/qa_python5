from conftest import *
from selenium.webdriver.common.by import By
import XPATH


def test_go_to_personal_account(driver, go_to_personal_account):
    accept_button = driver.find_elements(By.XPATH, XPATH.accept_button)
    return len(accept_button) > 0, driver.close()


def test_transition_from_personal_account_to_the_constructor(driver, go_to_personal_account):
    constructor_button = driver.find_element(By.XPATH, XPATH.constructor_button)
    constructor_button.click()
    assert driver.find_element(By.XPATH, XPATH.assemble_the_burger).text == "Соберите бургер"
    driver.close()


def test_transition_from_personal_account_by_logo(driver, go_to_personal_account):
    logo_button = driver.find_element(By.XPATH, XPATH.logo_button)
    logo_button.click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.close()
