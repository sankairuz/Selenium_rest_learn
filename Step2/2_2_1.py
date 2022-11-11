from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    result = int(x)+int(y)
    time.sleep(1)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(result))
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(5)
    browser.quit()