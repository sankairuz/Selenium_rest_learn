import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    browser.execute_script('window.scrollBy(0, 100);')
    browser.find_element(By.ID, 'answer').send_keys(str(calculate(x)))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    browser.close()
