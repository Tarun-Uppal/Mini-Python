import time
import webbrowser as web
import pyautogui as pg
from urllib.parse import quote


phone_no = '+919819719688'
message = 'This message was sent using python'

pg.FAILSAFE = False
parsedMessage = quote(message)
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(2)
width,height = pg.size()
pg.click(width/2,height/2)
time.sleep(3)
pg.press('enter')