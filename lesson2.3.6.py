from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".trollface").click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    input3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

finally:
    time.sleep(10)
    browser.close
    browser.quit
