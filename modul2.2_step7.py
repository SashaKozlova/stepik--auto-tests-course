from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome("/home/sasha/Downloads/chromedriver_linux64/chromedriver")
browser.get(link)

input_name = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
input_lastname = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
input_email = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
input_choose_file = browser.find_element_by_css_selector("input[type='file']")

current_dir = os.path.abspath(os.path.dirname('file.txt'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(os.path.abspath('file.txt'))
print(os.path.abspath(os.path.dirname('file.txt')))

input_name.send_keys('Sasha')
input_lastname.send_keys('Lastname')
input_email.send_keys('test@mail.ru')
input_choose_file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
