from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path = r'C:\Users\SOLO\Downloads\geckodriver.exe')
browser.get('https://play2048.co')

htmlElem = browser.find_element_by_tag_name('html')
for i in range(10):
    htmlElem.send_keys(Keys.UP)
    time.sleep(1)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(1)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(1)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(1)

