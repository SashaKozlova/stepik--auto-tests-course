from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")
browser.get(link)

element1 = browser.find_element_by_css_selector(".first_block .first_class > input:nth-child(2)")
element1.send_keys("name")
element2 = browser.find_element_by_css_selector(".first_block .second_class > input:nth-child(2)")
element2.send_keys("second")
element3 = browser.find_element_by_css_selector(".first_block .third_class > input:nth-child(2)")
element3.send_keys("third")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
