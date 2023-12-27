import time

from conftest import *
from selenium.webdriver.common.by import By
import XPATH


# Registration
def test_registration(driver):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_button = driver.find_element(By.XPATH, XPATH.registration_button)
    registration_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sob4444aka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('sob4444aka@ya.ru')
    registration_password_button = driver.find_element(By.XPATH, XPATH.registration_password_button)
    registration_password_button.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'  # по логике сайта, после успешной регистрации, пользователя перебрасывает на страничку авторизации)
    driver.quit()


# Sign in
def test_sign_in(driver):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_error_password(driver):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('12345')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    error_password_text = driver.find_element(By.XPATH, XPATH.error_password_text)
    assert error_password_text.text == 'Некорректный пароль'
    driver.quit()


def test_personal_area_log_in(driver):
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    driver.implicitly_wait(1)
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_sign_in_after_registration(driver):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    registration_button = driver.find_element(By.XPATH, XPATH.registration_button)
    registration_button.click()
    login_registration = driver.find_element(By.XPATH, XPATH.login_registration)
    login_registration.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


def test_sign_in_by_password_recovery_button(driver):
    login_button = driver.find_element(By.XPATH, XPATH.login_button)
    login_button.click()
    password_recovery_button = driver.find_element(By.XPATH, XPATH.password_recovery_button)
    password_recovery_button.click()
    login_registration = driver.find_element(By.XPATH, XPATH.login_registration)
    login_registration.click()
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
    user_password_or_registration_mail = driver.find_element(By.XPATH, XPATH.user_password_or_registration_mail)
    user_password_or_registration_mail.send_keys('123456')
    accept_button = driver.find_element(By.XPATH, XPATH.accept_button)
    accept_button.click()
    personal_area_button = driver.find_element(By.XPATH, XPATH.personal_area_button)
    personal_area_button.click()
    profile_button = driver.find_elements(By.XPATH, XPATH.profile_button)
    return len(profile_button) > 0, driver.quit()


# тест выхода из аккаунта проходит через раз, хоть я и добавил ожидание
def test_logout(driver, go_to_personal_account):
    registration_name_button = driver.find_element(By.XPATH, XPATH.registration_name_button)
    registration_name_button.send_keys('sobaka@ya.ru')
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
