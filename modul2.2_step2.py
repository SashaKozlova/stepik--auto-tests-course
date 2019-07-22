from selenium import webdriver
# from selenium.webdriver.support.ui import Select
import math


def calc(z):
    return str(math.log(abs(12*math.sin(int(z)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")
browser.get(link)

button_want_to_journey = browser.find_element_by_css_selector('button[type="submit"]')
button_want_to_journey.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
# confirm = browser.switch_to.alert
# confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# """SCROLLING"""
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# browser.execute_script("window.scrollBy(0, 100);")

input_result = browser.find_element_by_id("answer")
input_result.send_keys(y)

# option1 = browser.find_element_by_css_selector('[for="robotCheckbox"]')
# option1.click()
#
# radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
# radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

# browser.execute_script("window.scrollBy(0, 100);")
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView();

# link = "http://suninjuly.github.io/selects2.html"
# browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")
# browser.get(link)
#
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# number1 = browser.find_element_by_css_selector("h2 .nowrap#num1")
# num1 = number1.text
# number2 = browser.find_element_by_css_selector("h2 .nowrap#num2")
# num2 = number2.text
# result = int(num1) + int(num2)
# result = str(result)
# select = Select(browser.find_element_by_id("dropdown"))
# select.select_by_value(result)
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
