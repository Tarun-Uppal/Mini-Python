# imports all the things that could happen
from selenium.webdriver.support import expected_conditions as EC
# gets all the actions that the bot can do
from selenium.webdriver.common.action_chains import ActionChains  
# the webdriver wait
from selenium.webdriver.support.ui import WebDriverWait
# imports the options
from selenium.webdriver.chrome.options import Options
# imports the options for selenium
from selenium.common import exceptions 
# imports the keyboard and text part of selenium
from selenium.webdriver.common.keys import Keys 
# imports the webdriver 
from selenium import webdriver  
# imports os for the directory management
import os
# random imports
import re
# imports time
import time


# chrome path driver
chrome_path = os.path.dirname(__file__) + r'\chromedriver.exe'
# link for whatsapp web
Link = "https://web.whatsapp.com/"
# stores the browser
browser = None

# send messages and attachments
def sender(numbers, contacts, attachment_path):
    """
    sends the contacts the message
    """
    # gets the required varibles from the file
    global browser
    # the number of numbers to send the message to
    numbers_size = len(numbers)
    # login into whtsapp
    open_whatsapp()
    # sets the starting point
    i = 0   
    # makes a loop
    while True: 
        # gets the phone number form the database  
        number = numbers[i]
        # checks if the number is invaild
        if isValid(910000000000+number == False) or len(str(number)) != 10:
            # print("Invalid Number")
            print(number)
        # otherwise
        else:
            # print(contacts[i])
            # generates the personalized message
            message = "Dear " + str(contacts[i]) + "\n\nOver 50+ international products on sale at reasonable prices, visit www.edutess.com/shop/ to buy now"
            # generates the link
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(910000000000+number)
            # sends the generated link to the browser
            browser.get(link)
            # print("Sending message to", str(number))
            # sends the attachment
            send_attachment(attachment_path)
            # waits for 1 second
            time.sleep(1)
            # sends the message
            try:
                input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                for ch in message:
                    if ch == "\n":
                        ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                            Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                    else:
                        input_box.send_keys(ch)
                input_box.send_keys(Keys.ENTER)
                print("Message sent successfully")
            except Exception as e:
                print("Failed to send message exception: ", e)
                return
            # waits for 1 second
            time.sleep(1)
        # print(number)
        # checks if the array is over
        if i == numbers_size - 1:
            break
        # increments
        i += 1
    # exits the browser
    browser.quit()
    
def isValid(s):
    """
    validates the number
    """
    # casts the number into a string
    s = str(s)
    # atores the pattern
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    # validates the pattern and returns thue if it is valid otherwise false
    if (Pattern.match(s)) and len(s) == 12: 
        return True
    else:
        return False
    
def send_message(target, message, browser):
    """
    sends the message to the target number
    """
    global exceptions
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        ct = 0
        while ct != 5:
            try:
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                break
            except Exception as e:
                print("Retry Send Message Exception", e)
                ct += 1
        while True:
            try:
                input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                break
            except exceptions.NoSuchElementException as e:
                time.sleep(1)
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
        time.sleep(1)
    except exceptions.NoSuchElementException as e:
        print("send message exception: ", e)
        return
    
def send_attachment(file_path):
    global time, exceptions
    while True:
        try:
            attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
            attachment_box.click()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
    while True:
        try:
            image_box = browser.find_element_by_xpath(
                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(file_path)
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
    time.sleep(4)
    action = ActionChains(browser) 
    action.send_keys(Keys.ENTER).perform()
    
    print("File sent")
    
def open_whatsapp():
    """
    logs into whatsapp
    """
    global wait, browser
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    # if headless == 'True':
    #     chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    # browser.get(Link)
    # browser.maximize_window()
    # print("QR scanned")
    
def whatsapp_login():
    """
    logs into whatsapp
    """
    global wait, browser
    chrome_options = Options()
    folder_to_delete = os.path.dirname(__file__)
    folder_to_delete1 = folder_to_delete.split("\\")
    folder_to_delete_length = len(folder_to_delete1)
    folder_to_delete.replace(folder_to_delete, folder_to_delete1[folder_to_delete_length-1])
    print(folder_to_delete)
    chrome_options.add_argument('--user-data-dir=./User_Data')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    browser.get(Link)
    browser.maximize_window()