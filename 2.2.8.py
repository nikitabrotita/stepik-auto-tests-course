from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html" 
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("petrov@mail.ru")


    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # имя файла, который будем загружать на сайт
    file_name = "file.txt"

    # получаем путь к file.txt
    file_path = os.path.join(current_dir, file_name)

    # отправляем файл
    upload = browser.find_element_by_id("file")
    upload.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

                                            
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
