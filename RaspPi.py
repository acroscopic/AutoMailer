# AutoMailer script v5.0
# This script sends me scheduled emails to remind me to do stuff so I can swipe them away on my phone as I do them

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

sender_email = input("Please enter the sending email")
receiver_email = input("Please enter the receiving email")
password = getpass.getpass("Input password and press enter:")

startup = [
f"""Subject:Greetings Human!
Thank you for starting the AM daily email service
{start}"""
]

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
Trig 1-2:30
Go to the gym
""",

f"""Subject:Tuesday
Go to the gym, run 2 miles!
""",

f"""Subject:Wednesday
Physics 8-10:30
Trig 1-2:30
Go to the gym
""",

f"""Subject:Thursday
Run 2 miles!
""",

f"""Subject:Friday
Bike or run!
Weight lifting, 50 Squats, 50 Lunges, 100 Bicycle Kicks
""",

f"""Subject:Saturday
100 jumping jacks, yoga
""",

f"""Subject:Sunday
Run 10k!
Do Laundry, Dishes, and Trash"""
]

np.save("./numpyemails/startup.npy", startup)
np.save("./numpyemails/weekly.npy", weekly)
np.save("./numpyemails/daily.npy", daily)

def Startup():
        now = datetime.now()
        logtime = now.strftime("%m/%d/%y - %H:%M:%S")
        with smtplib.SMTP(smtp, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                emails = np.load("./numpyemails/startup.npy")
                print("Send reminders out now?")
                reply = str(input('y/n:')).lower().strip()
                if reply[0] == 'y':
                        Daily()
                        Weekly()
                if reply[0] != 'y':
                        pass
                for i in emails:
                        server.sendmail(sender_email, receiver_email, i)
        print(f"LOG: startup email sent at {logtime}")

def Daily():
        now = datetime.now()
        logtime = now.strftime("%m/%d/%y - %H:%M:%S")
        with smtplib.SMTP(smtp, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
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
                emails = np.load("./numpyemails/weekly.npy") #loading emails
                for idx, i in enumerate(emails): #idx fetches the index of workout.npy using enumerate
                        if idx != weekday: #if the index does not = the current day, skip it
                                continue
                        server.sendmail(sender_email, receiver_email, i) #sends the correct email
                        if idx == weekday: #if the index does = the current day, stop
                                break
                print(f"LOG: Weekly emails sent at {logtime}")

schedule.every().day.at("05:00").do(Daily)
schedule.every().day.at("05:00").do(Weekly)
Startup()

while True:
    schedule.run_pending()
    time.sleep(1)
