from selenium import webdriver
from time import sleep  
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(r'P:\Mini-Python\whatsapp-sender\attachments\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath (images/video): ')
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

action = ActionChains(driver) 
action.send_keys(Keys.ENTER).perform()

name = input('Enter the name of user or group : ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath(
    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

action = ActionChains(driver) 
action.send_keys(Keys.ENTER).perform()