import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    browser.find_element(By.NAME, 'firstname').send_keys('Ilya')
    browser.find_element(By.NAME, 'lastname').send_keys('Panin')
    browser.find_element(By.NAME, 'email').send_keys('Ilya@panin.ru')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()





finally:
    time.sleep(10)
    browser.quit()
