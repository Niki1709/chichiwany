import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(1)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    time.sleep(1)
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    time.sleep(1)
    input4 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    input4.click()
finally:
    time.sleep(15)
    browser.close
    browser.quit
