import math

from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_class_name("btn-primary")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
