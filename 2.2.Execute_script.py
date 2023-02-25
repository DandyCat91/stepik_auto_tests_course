from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    browser.get(link)
    x=int((browser.find_element(By.ID, "input_value")).text)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(15)
    browser.quit()