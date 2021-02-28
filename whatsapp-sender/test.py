import time
import webbrowser as web
import pyautogui as pg
from urllib.parse import quote


phone_no = '+919819719688'
message = 'hi'

def sendWhatsappMessage(phone_no, message):
	pg.FAILSAFE = False
	parsedMessage = quote(message)
	web.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + parsedMessage)
	time.sleep(2)
	width, height = pg.size()
	pg.click(width / 2,height / 2)
	time.sleep(10)
	pg.press('enter')

for i in range(1):
	sendWhatsappMessage(phone_no, message)
	print(i)
