from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # click the button to activate alert
    button = browser.find_element_by_id("button")
    button.click()

   
finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()
