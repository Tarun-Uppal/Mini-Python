from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# excel file reader
from pathlib import Path
import openpyxl
try:
    import autoit
except ModuleNotFoundError:
    pass
import time

chrome_default_path = r'P:\Mini-Python\whatsapp-sender\final\chromedriver.exe'

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None
choice = None
docChoice = None
doc_filename = r'P:\Mini-Python\whatsapp-sender\final\ME.jpeg'
unsaved_Contacts = None
filePath = r'P:\Mini-Python\whatsapp-sender\final\ME.jpeg'


def main():
    global message
    print("Web Page Open")
    (names, unsaved_Contacts) = read_file(r'P:\Mini-Python\whatsapp-sender\messageBlaster\Contacts.xlsx') 
    message = "Hi"

    # # Send Attachment Media only Images/Video
    # choice = input("Would you like to send attachment(yes/no): ")

    # docChoice = input("Would you file to send a Document file(yes/no): ")
    # if (docChoice == "yes"):
    #     # Note the document file should be present in the Document Folder
    #     doc_filename = input("Enter the Document file name you want to send: ")

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login(r'P:\Mini-Python\whatsapp-sender\final\chromedriver.exe', False)

    sender()
    print("Task Completed")
    browser.quit()
    
def read_file(filePath):
	xlsx_file = Path(filePath)
	wb_obj = openpyxl.load_workbook(xlsx_file) 

	# Read the active sheet:
	sheet = wb_obj.active
	# A and C from 2 to count
	# print(sheet["A3"].value)
	noOfEntries = sheet.max_row
	contacts = [noOfEntries]
	numbers = [noOfEntries]

	for i in range(noOfEntries):
		# print(str(sheet["A"+str(i+1)].value) + "- " + str(sheet["C"+str(i+1)].value))
		contacts.append(sheet["A"+str(i+1)].value)
		numbers.append(sheet["C"+str(i+1)].value)

	return (contacts, numbers)

# def input_contacts():
#     global Contact, unsaved_Contacts
#     # List of Contacts
#     Contact = []
#     unsaved_Contacts = []
#     while True:
#         # Enter your choice 1 or 2
#         print("PLEASE CHOOSE ONE OF THE OPTIONS:\n")
#         print("1.Message to Saved Contact number")
#         print("2.Message to Unsaved Contact number\n")
#         x = int(input("Enter your choice(1 or 2):\n"))
#         print()
#         if x == 1:
#             n = int(input('Enter number of Contacts to add(count)->'))
#             print()
#             for i in range(0, n):
#                 inp = str(input("Enter contact name(text)->"))
#                 inp = '"' + inp + '"'
#                 # print (inp)
#                 Contact.append(inp)
#         elif x == 2:
#             n = int(input('Enter number of unsaved Contacts to add(count)->'))
#             print()
#             for i in range(0, n):
#                 inp = str(input(
#                     "Enter unsaved contact number with country code(interger):\n\nValid input: 91943xxxxx12\nInvalid input: +91943xxxxx12\n\n"))
#                 unsaved_Contacts.append(inp)

#         choi = input("Do you want to add more contacts(y/n)->")
#         if choi == "n":
#             break

#     if len(Contact) != 0:
#         print("\nSaved contacts entered list->", Contact)
#     if len(unsaved_Contacts) != 0:
#         print("Unsaved numbers entered list->", unsaved_Contacts)
#     input("\nPress ENTER to continue...")


# def input_message():
#     global message
#     # Enter your Good Morning Msg
#     print(
#         "Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
#     message = []
#     done = False

#     while not done:
#         temp = input()
#         if len(temp) != 0 and temp[-1] == "~":
#             done = True
#             message.append(temp[:-1])
#         else:
#             message.append(temp)
#     message = "\n".join(message)
#     print(message)


def whatsapp_login(chrome_path, headless):
    global wait, browser, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    if headless == 'True':
        chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")

def send_message(target):
    global message, wait, browser
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

def send_attachment():
    attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    
    image_box = browser.find_element_by_xpath(
		'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filePath)
    
    time.sleep(3)
    
    action = ActionChains(browser) 
    action.send_keys(Keys.ENTER).perform()
    
    print("File sent")

# send messages and attachments
def sender():
    global Contact, choice, docChoice, unsaved_Contacts
    print(Contact, unsaved_Contacts)
    for i in Contact:
        try:
            send_message(i)
            print("Message sent to ", i)
        except Exception as e:
            print("Msg to {} send Exception {}".format(i, e))
        if (choice == "yes"):
            try:
                send_attachment()
            except:
                print('Attachment not sent.')
        if (docChoice == "yes"):
            try:
                send_files()
            except:
                print('Files not sent')
    time.sleep(5)
    if len(unsaved_Contacts) > 0:
        for i in unsaved_Contacts:
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(i)
            # driver  = webdriver.Chrome()
            browser.get(link)
            print("Sending message to", i)
            send_unsaved_contact_message()
            if (choice == "yes"):
                try:
                    send_attachment()
                except:
                    print()
            # if (docChoice == "yes"):
            #     try:
            #         send_files()
            #     except:
            #         print()
            time.sleep(7)
    
def send_unsaved_contact_message():
    global message
    try:
        time.sleep(10)
        browser.implicitly_wait(10)
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