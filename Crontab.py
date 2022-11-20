# AutoMailer script v5.0
# This script is meant to set up with crontab

#       _______       ______  ___
#       ___    |      ___   |/  /
#       __  /| |      __  /|_/ / 
#       _  ___ |      _  /  / /  
#       /_/  |_|      /_/  /_/   

import os
import ssl
import time
import random
import getpass
import smtplib
import schedule
import requests
import threading
import numpy as np
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.now()
start = now.strftime("%m/%d/%y - %H:%M:%S")
smtp = ("smtp.gmail.com")
port = (587)
context=ssl.create_default_context()

# If you want to use with crontab, you must hardcode in your emails and password
# Note that this is inherently insecure, use at your own risk.
sender_email = ("Email1@gmail.com")
receiver_email = ("Email2@gmail.com")
password = ("Password123")

daily = [
f"""Subject:Math & Physics!""",
f"""Subject:Study German!""",
f"""Subject:Study Russian!""",
f"""Subject:Read!""",
f"""Subject:Meditate!""",
f"""Subject:Journal!"""
]

weekly = [
f"""Subject:Monday
Physics 8-10:30
ASL 12-1
Trig 1-2:30
ASL 5:30-8:30
Go to the gym
""",

f"""Subject:Tuesday
Go to the gym, run
""",

f"""Subject:Wednesday
Physics 8-10:30
Trig 1-2:30
Go to the gym, """,

f"""Subject:Thursday
Run 2 miles!
""",

f"""Subject:Friday
Bike or run!
Weight lifting, 50 Squats, 50 Lunges, 100 Bicycle Kicks""",

f"""Subject:Saturday
100 jumping jacks, yoga""",

f"""Subject:Sunday
Run 10k!
Do Laundry, Dishes, and Trash"""
]

np.save("/home/x/Desktop/documents/bin/DRM/v5/numpyemails/weekly.npy", weekly)
np.save("/home/x/Desktop/documents/bin/DRM/v5/numpyemails/daily.npy", daily)

def Daily():
        now = datetime.now()
        logtime = now.strftime("%m/%d/%y - %H:%M:%S")
        with smtplib.SMTP(smtp, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
              
                # change the email location to where you want to store them if using crontab. 
                emails = np.load("./numpyemails/daily.npy")
                
                for i in emails:
                        server.sendmail(sender_email, receiver_email, i)
                        time.sleep(3)
        print(f"LOG: Daily emails sent at {logtime}")

def Weekly():
        now = datetime.now()
        logtime = now.strftime("%m/%d/%y - %H:%M:%S")
        weekday = (datetime.today().weekday()) #what day of the week it is
        with smtplib.SMTP(smtp, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password) #logging in
              
                # change the email location to where you want to store them if using crontab.
                emails = np.load("./numpyemails/weekly.npy") #loading emails
                
                for idx, i in enumerate(emails): #idx fetches the index of workout.npy using enumerate
                        if idx != weekday: #if the index does not = the current day, skip it
                                continue
                        server.sendmail(sender_email, receiver_email, i) #sends the correct email
                        if idx == weekday: #if the index does = the current day, stop
                                break
                print(f"LOG: Weekly emails sent at {logtime}")

Daily()
Weekly()
