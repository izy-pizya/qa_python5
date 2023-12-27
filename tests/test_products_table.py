from conftest import *
from selenium.webdriver.common.by import By
import XPATH


# go to sauce
def test_go_to_sauce(open_hello_window):
    sauce_button = driver.find_element(By.XPATH, XPATH.sauce_button)
    sauce_button.click()
    assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Соусы'
    driver.quit()


# go to fillings
def test_go_to_fillings(open_hello_window):
    fillings_button = driver.find_element(By.XPATH, XPATH.fillings_button)
    fillings_button.click()
    assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Начинки'
    driver.quit()


# go to fillings
def test_go_to_rolls(open_hello_window):
    fillings_button = driver.find_element(By.XPATH, XPATH.fillings_button)
    fillings_button.click()
    rolls_button = driver.find_element(By.XPATH, XPATH.rolls_button)
    rolls_button.click()
    assert driver.find_element(By.XPATH, XPATH.selected_element).text == 'Булки'
    driver.quit()
