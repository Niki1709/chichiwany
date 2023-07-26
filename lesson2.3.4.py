from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    input3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

finally:
    time.sleep(10)
    browser.close
    browser.quit
    
    
    
    
