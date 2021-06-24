from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html" 
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int(browser.find_element_by_css_selector("#input_value").text)
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))
    
    checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

                                            
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
