import sys
import getpass
import smtplib, ssl
import requests
import numpy as np

port = 465
context = ssl.create_default_context()

sender_email = input("Please enter the sending email")
password = getpass.getpass("Input password and press enter:")
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
