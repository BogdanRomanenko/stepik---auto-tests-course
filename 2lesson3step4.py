from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # click the button to activate alert
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # confirm alert
    confirm = browser.switch_to.alert
    confirm.accept()

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
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()
