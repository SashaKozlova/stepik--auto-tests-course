from selenium import webdriver
import math


def calc(z):
    return str(math.log(abs(12*math.sin(int(z)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")
browser.get(link)

x_element = browser.find_element_by_css_selector("img")
x = x_element.get_attribute('valuex')
y = calc(x)

input_result = browser.find_element_by_id("answer")
input_result.send_keys(y)

human_radio = browser.find_element_by_id("humanRule")
human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
assert human_checked is not None, "Human radio is not selected by default"
robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robot radio: ", robots_checked)
assert robots_checked is None

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
browser.quit()
