from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #wait till needed price displayed
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # click the button to book the house
    button = browser.find_element_by_css_selector("#book")
    button.click()

    # time sleep - wait the next page downloaded
    time.sleep(1)

    # find a value of x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # put the x value in the answer field
    answer_field = browser.find_element_by_css_selector("#answer")
    answer_field.send_keys(y)

    #send the form
    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()
