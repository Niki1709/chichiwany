from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
    return str(int(x)+int(z))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.ID, "num1")
    x = x1.text
    x2 = browser.find_element(By.ID, "num2")
    z = x2.text
    y = calc(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))
    input3 = browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

finally:
    time.sleep(15)
    browser.close
    browser.quit
    
    
