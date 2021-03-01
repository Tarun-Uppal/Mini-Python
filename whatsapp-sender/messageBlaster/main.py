# selenium imports
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# imports the keyboard and text part of selenium
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium import webdriver  
# excel file reader
from pathlib import Path
import openpyxl
# random imports
import time
try:
    import autoit
except ModuleNotFoundError:
    pass

# link for whatsapp
Link = "https://web.whatsapp.com/"
# stores the browser
browser = None
chrome_path = r'P:\Mini-Python\whatsapp-sender\messageBlaster\chromedriver.exe'
contacts_path = r'P:\Mini-Python\whatsapp-sender\messageBlaster\Contacts.xlsx'
attachment_path = r'P:\Mini-Python\whatsapp-sender\attachments\Sale.mp4'
wait = None

def main():
    (contacts, numbers) = read_file()
    sender(numbers, contacts)
    
# send messages and attachments
def sender(numbers, contacts):
    global browser, attachment_path, time
    numbers_size = len(numbers)
    whatsapp_login(False)
    for i in range(numbers_size):
        number = numbers[i]
        if number == 2:
            print("Invalid Number")
        else:
            message = "Dear " + contacts[i] + "\n\nOver 50+ international products on sale at reasonable prices, visit www.edutess.com/shop/ to buy now"
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(910000000000+number)
            browser.get(link)
            print("Sending message to", str(number))
            send_attachment(attachment_path)
            time.sleep(1)
            send_unsaved_contact_message(message)
            time.sleep(1)
        print(number)
    browser.quit()
    
def read_file():
    global contacts_path
    xlsx_file = Path(contacts_path)
    wb_obj = openpyxl.load_workbook(xlsx_file) 

    sheet = wb_obj.active
    entries_count = sheet.max_row
    contacts = [entries_count]
    numbers = [entries_count]
    for i in range(entries_count):
        contacts.append(sheet["A" + str(i+1)].value)
        numbers.append(sheet["C" + str(i+1)].value)
    return (contacts, numbers)

def whatsapp_login(headless):
    global wait, browser
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    if headless == True:
        chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")
    
def send_message(target, message, browser):
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
                time.sleep(3)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
        time.sleep(1)
    except NoSuchElementException as e:
        print("send message exception: ", e)
        return
    
def send_attachment(file_path):
    global time
    time.sleep(4)
    attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    
    image_box = browser.find_element_by_xpath(
		'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(file_path)
    
    time.sleep(4)
    
    action = ActionChains(browser) 
    action.send_keys(Keys.ENTER).perform()
    
    print("File sent")
    
def send_unsaved_contact_message(message):
    try:
        browser.implicitly_wait(8)
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

main()
    
