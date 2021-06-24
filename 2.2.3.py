from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html" 
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element_by_css_selector("#num1").text)
    num2 = int(browser.find_element_by_css_selector("#num2").text)
    summary = str(num1 + num2)
    
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summary)

    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

                                            
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
