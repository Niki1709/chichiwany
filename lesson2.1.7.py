import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_r = browser.find_element(By.ID, "treasure")
    x_element = x_r.get_attribute("valuex")
    x = x_element
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
