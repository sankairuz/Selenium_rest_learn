import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.NAME, 'text').send_keys(calculate(x))
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(5)
    browser.quit()
