from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(z):
    return str(math.log(abs(12*math.sin(int(z)))))


browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element_by_id("book")
WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

button.click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
print(x)
y = calc(x)

input_result = browser.find_element_by_id("answer")
input_result.send_keys(y)
button_submit = browser.find_element_by_id("solve")
button_submit.click()
