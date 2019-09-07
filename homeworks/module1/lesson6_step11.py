from selenium import webdriver
import time

try: 
    # valid page
    # link = "http://suninjuly.github.io/registration1.html"

    # page with a bug
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill the required fields of the form
    first_name = browser.find_element_by_css_selector(".first_block input.first")
    first_name.send_keys("In")
    last_name = browser.find_element_by_css_selector(".first_block input.second")
    last_name.send_keys("P")
    email = browser.find_element_by_css_selector(".first_block input.third")
    email.send_keys("Sm")

    #send the form
    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

    # sleep time - wait until a new web page opened
    time.sleep(1)

    # find expected element
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # assign the found value to a variable
    welcome_text = welcome_text_elt.text

    # compare expected text with actually found text
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('great')

finally:
    # time sleep - to see the result
    time.sleep(10)
    # quit the browser
    browser.quit()