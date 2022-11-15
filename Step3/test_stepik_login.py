import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = 'https://stepik.org/lesson/236895/step/1'
urls = ['https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestStepik:

    def test_stepik(self, browser):
        browser.get(link)
        browser.implicitly_wait(10)
        # ждём когда кнопка войти станет активной
        button_login = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.navbar__auth_login')))
        button_login.click()
        # логинимся
        browser.find_element(By.ID, 'id_login_email').send_keys('sankairuz@gmail.com')
        browser.find_element(By.ID, 'id_login_password').send_keys('POtato95')
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()

        # ждём когда поле ввода станет активным и вводим ответ

        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer())
        button_login = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        button_login.click()
        # проверяем результат

        result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        assert result == 'Correct!', f'А вот это мы соберем = {result}'

    @pytest.mark.parametrize('new_url', urls)
    def test_long(self, browser, new_url):
        browser.get(new_url)
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer())

        button_login = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        button_login.click()
        # проверяем результат

        result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        assert result == 'Correct!', f'А вот это мы соберем = {result}'
