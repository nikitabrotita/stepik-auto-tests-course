from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html" 
    browser = webdriver.Chrome()
    browser.get(link)
    
    image = browser.find_element_by_css_selector("img")
    x_element = image.get_attribute("valuex")
   
    y = calc(x_element)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    
    checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

                                            
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
