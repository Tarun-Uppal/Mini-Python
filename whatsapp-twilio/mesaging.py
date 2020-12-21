# usage git bash : python P:/Mini-Python/whatsapp-automation/mesaging.py 
import os
from twilio.rest import Client
# from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
account_sid = "ACa5d4cc6e3e43db5e1985cc37e4609fc8"
auth_token = "your token"
client = Client(account_sid, auth_token)

my_msg = "temp"

message = client.messages.create(to='whatsapp:+917304298382', from_='whatsapp:+14155238886',
                                     body=my_msg)
