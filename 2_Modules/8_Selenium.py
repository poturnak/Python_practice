#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# ______________________Selenium module ______________________
# First off you need to import selenium
# You need to use 'from selenium import webdriver'
# variable = webdriver.driver_class() - then you can create variable with certain browser class
# variable.get() - will open URL with the chosen browser
# ______________________Selenium search ______________________
# find_element - search for 1 object that firt matches your query
# find_elements - retunrs all objects that match your query
# If selenium does not find anything it raises an exception 'NoSuchElement'
# if you do not want program to crash use try except
# --------Elements that use CSS class name
# browser.find_element_by_class_name(name)
# browser.find_elements_by_class_name(name)
# --------Elements that match the CSS selector
# browser.find_element_by_css_selector(selector)
# browser.find_elements_by_css_selector(selector)
# --------Elements with a matching id attribute value
# browser.find_element_by_id(id)
# browser.find_elements_by_id(id)
# --------<a> elements that completely match the text provided
# browser.find_element_by_link_text(text)
# browser.find_elements_by_link_text(text)
# --------<a> elements that contain the text provided
# browser.find_element_by_partial_link_text(text)
# browser.find_elements_by_partial_link_text(text)
# --------Elements with a matching name attribute value
# browser.find_element_by_name(name)
# browser.find_elements_by_name(name)
# --------Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')
# browser.find_element_by_tag_name(name)
# browser.find_elements_by_tag_name(name)
# ______________________Attributes or methods for selenium object ______________________
# tag_name              - The tag name, such as 'a' for an <a> element
# get_attribute(name)   - The value for the element’s name attribute
# text                  - The text within the element, such as 'hello' in <span>hello</span>
# clear()               - For text field or text area elements, clears the text typed into it
# is_displayed()        - Returns True if the element is visible; otherwise returns False
# is_enabled()          - For input elements, returns True if the element is enabled; otherwise returns False
# is_selected()         - For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
# location              - A dictionary with keys 'x' and 'y' for the position of the element in the page
# click() - click on the link
# send_key() - sending keystrokes to the forms on the webpage
# submit() - submit or click the button
# clear() - if you entered something in the text form, clear() method will delete the text
# ______________________Module for sending special keys ______________________
# You need to import it first
# from selenium.webdriver.common.keys import Keys
# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT - The keyboard arrow keys
# Keys.ENTER, Keys.RETURN - The ENTER and RETURN keys
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP - The home, end, pagedown, and pageup keys
# Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE - The ESC, BACKSPACE, and DELETE keys
# Keys.F1, Keys.F2,..., Keys.F12 - The F1 to F12 keys at the top of the keyboard
# Keys.TAB - The TAB key
# --an example is element.send_key(Key.ENTER)
# ______________________Clicking brower buttons ______________________
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()
# ===================================================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found {} element with that class name'.format(elem.tag_name))
except:
    print('Was not able to find any elements')

linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()

# Filling out email form
# browser.get('https://mail.yahoo.com')
# emailElem = browser.find_element_by_id('login-username')
# emailElem.send_keys('not_my_real_email')
# buttonElem = browser.find_element_by_id('login-signin')
# buttonElem.click()
# passwordElem = browser.find_element_by_id('login-passwd')
# passwordElem.send_keys('password')
# passwordElem.submit()

# in this example you will send special keys to the browser
# first you find element by tag name
# html is very generalized
# then you can send special chanracters to browser

browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls to top
