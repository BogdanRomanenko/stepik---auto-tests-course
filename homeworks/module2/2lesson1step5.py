from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find a value of x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # put the x value in the answer field
    answer_field = browser.find_element_by_css_selector("#answer")
    answer_field.send_keys(y)

    # select the "I'm the robot" checkbox
    checkbox_robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox_robot.click()

    # select the "Robots rule" radiobutton
    radiobutton_robot = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton_robot.click()

    #send the form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()
