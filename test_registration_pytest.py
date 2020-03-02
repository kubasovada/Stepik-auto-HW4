from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

def test_register_new_user(browser):
    reg_user = 'testemail113{}@mail.ru'.format(random.randint(1, 500000))
    passw = 'GhbdtnCntgbr123'
    browser.find_element(By.ID, 'login_link').click()
    reg_email = browser.find_element(By.ID, 'id_registration-email')
    reg_email.clear()
    reg_email.send_keys(reg_user)
    reg_pass1 = browser.find_element(By.ID, 'id_registration-password1')
    reg_pass1.clear()
    reg_pass1.send_keys(passw)
    reg_pass2 = browser.find_element(By.ID, 'id_registration-password2')
    reg_pass2.clear()
    reg_pass2.send_keys(passw)
    browser.find_element(By.CSS_SELECTOR, '[name = "registration_submit"]').click()
    try:
        reg_t = browser.find_element(By.CSS_SELECTOR, '.alertinner.wicon').text
    except NoSuchElementException:
        reg_t = 'Страница не найдена'
    assert reg_t == 'Спасибо за регистрацию!', f'Got {reg_t} instead of "Спасибо за регистрацию!"'


