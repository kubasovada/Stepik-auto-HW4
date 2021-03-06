from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Вариант №1
def test_basket_button_display(browser):
    add_to_basket = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert add_to_basket.is_displayed(), 'Страница товара не содержит кнопку добавления в корзину'

# Вариант №2
def test_basket_button_display2(browser):
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button')), 'Basket button is not displayed')
        flag = True
    except (NoSuchElementException, TimeoutException):
        flag = False
    assert flag, 'Страница товара не содержит кнопку добавления в корзину'


