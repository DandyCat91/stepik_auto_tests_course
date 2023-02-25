from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x = int((browser.find_element(By.ID, "input_value")).text)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(15)
    browser.quit()