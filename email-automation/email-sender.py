import smtplib, ssl

# usage: git bash: python P:/Mini-Python/email-automation/email-sender.py

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "tarunpreetuppal2007@gmail.com"
receiver_email = "tarunpreetuppal2007@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)