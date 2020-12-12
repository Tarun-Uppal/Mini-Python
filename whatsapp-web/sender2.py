from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# python P:/Mini-Python/whatsapp-web/sender2.py

contact = "Sapna Uppal"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome('P:\Mini-Python\whatsapp-web\chromedriver')
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
inp_xpath_search = "//input[@title='Search or start new chat']"
print("inp temp")
input_box_search = WebDriverWait(driver,500).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
print('found element by xpath')
input_box_search.click()
print('clicked input box')
time.sleep(2)
print('waiting for 2 seconds')
input_box_search.send_keys(contact)
print('found contact')
time.sleep(2)
# waited 2 seconds
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
print('selected contact')
selected_contact.click()
print('selected contact')
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
driver.quit()