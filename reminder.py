#   _______       ______  ___
#   ___    |      ___   |/  /
#   __  /| |      __  /|_/ / 
#   _  ___ |      _  /  / /  
#   /_/  |_|      /_/  /_/   


import sys
import getpass
import smtplib, ssl
import requests

port = 465
context = ssl.create_default_context()

# Hardcode these in for easy access, although it is a security risk.
password = getpass.getpass("Input password and press enter:")
sender_email = input("Please enter the sending email")
receiver_email = input("Please enter the receiving email")

message = input("Please enter your message: ")

def Reminder():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        reminder = ["subject:" + message]
        for i in reminder:
            server.sendmail(sender_email, receiver_email, i)
            sys.exit("Reminder has been sent!")

Reminder()
