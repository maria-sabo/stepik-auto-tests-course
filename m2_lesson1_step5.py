from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # x_element = browser.find_element_by_id('input_value')
    # x = x_element.text
    chest = browser.find_element_by_css_selector("[valuex]")
    x = chest.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
