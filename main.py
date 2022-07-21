# DRM script v3.0
# This script sends me scheduled emails to remind me to do stuff so I can swipe them away on my phone as I do them

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

start = now.strftime("%m/%d/%y - %H:%M:%S")
smtp = ("smtp.gmail.com")
port = 587
context=ssl.create_default_context()

sender_email = input("Please enter the sending email")
receiver_email = input("Please enter the receiving email")
password = getpass.getpass("Input password and press enter:")

startup = [
f"""Subject:Greetings Human!
Thank you for starting the DRM daily email service
{start}"""
]

daily = [
f"""Subject:Math & Physics!""",
f"""Subject:Study German!""",
f"""Subject:Study Russian!""",
f"""Subject:Study ASL!""",
f"""Subject:Computer Science!""",
f"""Subject:Read!""",
f"""Subject:Write!""",
f"""Subject:Practice random hobby!""",
f"""Subject:Meditate!""",
f"""Subject:Journal!"""
]


weekly = [
f"""Subject:Monday
Go for a run!""",

f"""Subject:Tuesday
Go for a run!
Jiu Jitsu practice""",

f"""Subject:Wednesday
50 Pushups, 50 Situps, 50 Russian Twists, 30 Pullups, 15 Burpees""",

f"""Subject:Thursday
50 Pushups, 50 Situps, 50 Russian Twists, 30 Pullups, 15 Burpees,
Jiu Jitsu practice""",

f"""Subject:Friday
Weight lifting, 50 Squats, 50 Lunges, 100 Bicycle Kicks, 15 Burpees
Bike or run!""",

f"""Subject:Saturday
50 Pushups, 50 Situps, 50 Russian Twists, 30 Pullups, 15 Burpees""",

f"""Subject:Sunday
100 Jumping Jacks, Yoga Steches"""
]

#saving schedule a single folder
np.save("./numpyemails/startup.npy", startup)
np.save("./numpyemails/weekly.npy", weekly)
np.save("./numpyemails/daily.npy", daily)

def Startup():
        with smtplib.SMTP(smtp, port) as server: #opens up the gmail server connection
                server.starttls(context=context) #starts TLS encryption
                server.login(sender_email, password)
                emails = np.load("/home/pi/drm/numpyemails/startup.npy")
                print("Send reminders out now?")
                reply = str(input('y/n:')).lower().strip()
                if reply[0] == 'y': #If you reply Y/y it will send out all emails
                        Daily()
                        Weekly()
                if reply[0] != 'y': #if you say anything else it will only send the startup email
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
                emails = np.load("/home/pi/drm/numpyemails/daily.npy")
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
                emails = np.load("/home/pi/drm/numpyemails/weekly.npy") #loading emails
                for idx, i in enumerate(emails): #idx fetches the index of workout.npy using enumerate
                        if idx != weekday: #if the index does not = the current day, skip it
                                continue
                        server.sendmail(sender_email, receiver_email, i) #sends the correct email
                        if idx == weekday: #if the index does = the current day, stop the loop
                                break
                print(f"LOG: Weekly emails sent at {logtime}")

schedule.every().day.at("05:00").do(Daily)
schedule.every().day.at("05:00").do(Weekly)
Startup()

while True:
    schedule.run_pending()
    time.sleep(1)
