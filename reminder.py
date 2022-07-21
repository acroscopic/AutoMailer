#This is a script that runs once to send a 1 off reminder to the email, it's relatively simple because I don't use it often.

import os
import time
import sys
import getpass
import smtplib, ssl
import schedule
import threading
import random
import requests
import numpy as np
from datetime import date

t = date.today()
startdate = t.strftime("%m/%d/%y")

port = 465
context = ssl.create_default_context()

sender_email = input("Please enter the sending email")
password = getpass.getpass("Input password and press enter:")
receiver_email = input("Please enter the receiving email")
emailtime = input("Please enter the time you want to be reminded in 24 format: ")
message = input("Please enter your reminder message now: ")

def Reminder():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        reminder = ["subject:" + message]
        for i in reminder:
            server.sendmail(sender_email, receiver_email, i)
            sys.exit("Reminder has been sent!")

#Setting the time for each email array
schedule.every().day.at(emailtime).do(Reminder)


while True:
    schedule.run_pending()
    time.sleep(1)
