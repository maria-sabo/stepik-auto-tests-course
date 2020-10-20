import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    time.sleep(5)
    text_area = browser.find_element_by_css_selector(".textarea")

    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))

    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()

    ans = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'smart-hints__hint')))
    try:
        assert ans.text == 'Correct!', 'Not correct'
    except AssertionError:
        print(ans.text)

