from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    browser.get(link)
    x=int((browser.find_element(By.ID, "num1")).text)
    y=int((browser.find_element(By.ID, "num2")).text)
    z=str(x+y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

finally:
    time.sleep(15)
    browser.quit()