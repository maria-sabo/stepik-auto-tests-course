import math
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    solve = browser.find_element_by_id('solve')
    solve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
