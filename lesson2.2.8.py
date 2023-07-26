from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Nik")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Tik")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("NikTik@egg")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson.txt')
    print(os.path.abspath(os.path.dirname(__file__)))
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    input5 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(10)
    browser.close
    browser.quit
