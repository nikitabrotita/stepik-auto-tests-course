from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = WebDriverWait(browser, 12).until(
                     EC.text_to_be_present_in_element((By.ID,"price"), '$100')
                )
    if button == True:

        btn = browser.find_element_by_id('book')

        btn.click()
    
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(y))

    
    button_1 = browser.find_element_by_css_selector("#solve.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
    
    
    button_1.click()

                                            
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
