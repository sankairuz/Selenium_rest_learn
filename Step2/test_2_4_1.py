import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    btn = browser.find_element(By.ID, 'book')
    btn.click()

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.NAME, 'text').send_keys(calculate(x))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(10)
    browser.quit()
