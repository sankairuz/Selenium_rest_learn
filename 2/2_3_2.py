from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calculate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.NAME, 'text').send_keys(calculate(x))
    browser.find_element(By.CLASS_NAME, 'btn').click()









finally:
    time.sleep(10)
    browser.quit()