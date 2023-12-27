import time

from conftest import *
from selenium.webdriver.common.by import By
import XPATH


# Registration
def test_registration(open_hello_window):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_button = driver.find_element(By.XPATH, XPATH.registration_button)
    registration_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('11211212111assssss12ssa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('11211212111assssss12ssa@ya.ru')
    registration_password_button = driver.find_element(By.XPATH, XPATH.registration_password_button)
    registration_password_button.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'  # по логике сайта, после успешной регистрации, пользователя перебрасывает на страничку авторизации)
    driver.quit()


# Sign in
def test_sign_in(open_hello_window):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_error_password(open_hello_window):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('12345')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    error_password_text = driver.find_element(By.XPATH, XPATH.error_password_text)
    assert error_password_text.text == 'Некорректный пароль'
    driver.quit()


def test_personal_area_log_in(open_hello_window):
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    driver.implicitly_wait(1)
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_sign_in_after_registration(open_hello_window):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_button = driver.find_element(By.XPATH, XPATH.registration_button)
    registration_button.click()
    login_registration = driver.find_element(By.XPATH, XPATH.login_registration)
    login_registration.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_sign_in_by_password_recovery_button(open_hello_window):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    password_recovery_button = driver.find_element(By.XPATH, XPATH.password_recovery_button)
    password_recovery_button.click()
    login_registration = driver.find_element(By.XPATH, XPATH.login_registration)
    login_registration.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_logout(go_to_personal_account):
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sasasa@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_account = driver.find_element(By.XPATH, XPATH.personal_account)
    personal_account.click()
    time.sleep(1)
    logout_button = driver.find_element(By.XPATH, XPATH.logout_button)
    logout_button.click()
    time.sleep(1)
    accept_button = driver.find_elements(By.XPATH, XPATH.accept_button)
    return len(accept_button) > 0, driver.quit()




'''
    password_recovery_button_mail = driver.find_element()
    password_recovery_button_mail.send_keys('sasasa@ya.ru')
    time.sleep(5)
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('new password')
    letter_mail = driver.find_element(By.XPATH, XPATH.letter_mail)
    letter_mail.send_keys('код из письма')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    time.sleep(10)
'''
