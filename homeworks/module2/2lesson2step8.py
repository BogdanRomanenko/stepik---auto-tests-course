from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill the required fields of the form
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys("In")

    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys("P")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("Sm")

    file_download = browser.find_element_by_css_selector("#file")
    file_path = os.path.abspath ("C:/Users/User/Downloads/credits.txt")
    file_download.send_keys(file_path)

    # sleep time - wait until a file downloaded
    time.sleep(1)

    #send the form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()