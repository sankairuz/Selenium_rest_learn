import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, 'h2 img').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calculate(x))

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, '.btn').click()



finally:
    time.sleep(5)
    browser.quit()
