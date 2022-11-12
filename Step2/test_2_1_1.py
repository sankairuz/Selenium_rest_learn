import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    time.sleep(5)
    result = calc(x)
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()
    browser.find_element(By.CSS_SELECTOR, '.form-check-label').click()
    browser.find_element(By.CSS_SELECTOR, 'button').click()
finally:
    time.sleep(10)
    browser.quit()