from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find a value num1
    num1 = browser.find_element_by_css_selector("#num1")
    x = num1.text
    
    # find a value num2
    num2 = browser.find_element_by_css_selector("#num2")
    y = num2.text

    # count the summ of x and y
    summ = int(x) + int(y)
    print(summ)

    # slect the correct answer in dropdown
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_visible_text(str(summ))


    #send the form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()
