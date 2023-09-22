# AutoMailer script v6.0
# This script sends scheduled emails

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
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.now()
start = now.strftime("%m/%d/%y - %H:%M:%S")
smtp = ("smtp.gmail.com")
port = (587)
context=ssl.create_default_context()

#hardcoded emails and passwords (Security risk!)
sender_email = ("YourEmailHere@gmail.com")
receiver_email = ("OtherEmailHere@gmail.com")
password = ("REALpassword123")

sender_email = input("Please enter the sending email")
receiver_email = input("Please enter the receiving email")
password = getpass.getpass("Input password and press enter:")

weekly = [
"""Subject:Monday
Warm-up: Dynamic stretching for 5 minutes
Run: Interval Training
5-minute warm-up jog
Sprint for 30 seconds, then recover with a slow jog for 1 minute.
Repeat the sprint/recovery cycle for a total of 8-10 sets.
Strength Training:
Dumbbell Squats: 3 sets of 12 reps
Dumbbell Lunges: 3 sets of 12 reps (each leg)
Dumbbell Shoulder Press: 3 sets of 12 reps
Pull-ups (using the pull-up bar): 3 sets of 8 reps
Cool-down: Static stretching for 5-10 minutes""",

"""Subject:Tuesday
Warm-up: Dynamic stretching for 5 minutes
Run: Tempo Run
Start with a 5-minute warm-up jog.
Run at a comfortably hard pace (slightly faster than your regular pace) for 20-30 minutes.
Finish with a 5-minute cooldown jog.
Strength Training:
Dumbbell Deadlifts: 3 sets of 12 reps
Dumbbell Bench Press: 3 sets of 12 reps
Bent-Over Rows (using dumbbells): 3 sets of 12 reps
Hanging Leg Raises (using the pull-up bar): 3 sets of 10 reps
Cool-down: Static stretching for 5-10 minutes
""",

"""Subject:Wednesday
Rest day!
""",

"""Subject:Thursday
Warm-up: Dynamic stretching for 5 minutes
Run: Fartlek Training
After a 5-minute warm-up jog, alternate between periods of fast running and slower recovery jogs.
For example, sprint for 1 minute, then jog slowly for 2 minutes.
Repeat this cycle for a total of 6-8 sets.
Core Training:
Plank: Hold for 1 minute
Russian Twists (using a dumbbell): 3 sets of 15 reps (each side)
Bicycle Crunches: 3 sets of 15 reps (each side)
Leg Raises: 3 sets of 12 reps
Cool-down: Static stretching for 5-10 minutes
""",

"""Subject:Friday
Light cardio (Cycle for 30 minutes)
""",

"""Subject:Saturday
Yoga and Mobility Training:
Perform a 30-45 minute yoga routine focusing on flexibility, balance, and mobility.
Include poses like downward dog, warrior series, pigeon pose, and seated forward bends.
Incorporate dynamic movements and flows to improve your overall range of motion.
""",

"""Subject:Sunday
Warm-up: Dynamic stretching for 5 minutes
Run: Long Run
Start with a comfortable pace and gradually increase the duration each week.
Aim for a run of 45-60 minutes or a distance that challenges you.
Cool-down: Static stretching for 5-10 minutes
"""
]

startup = [
f"""Subject:Greetings Human!
Thank you for starting the AM daily email service
{start}"""
]


np.save("./numpyemails/weekly.npy", weekly)
np.save("./numpyemails/startup.npy", startup)


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
                        os.system('cls' if os.name == 'nt' else 'clear')
                        Daily()
                        Weekly()
                if reply[0] != 'y':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        pass
                for i in emails:
                        server.sendmail(sender_email, receiver_email, i)
        print(f"LOG: startup email sent at {logtime}")

def Daily():
        now = datetime.now()
        logtime = now.strftime("%m/%d/%y - %H:%M:%S")


        url = "https://www.dictionary.com/e/word-of-the-day/"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, "html.parser")
        word_of_the_day = soup.find('div', class_='otd-item-headword__word')
        wotd = word_of_the_day.text.strip()
        
        word_of_the_day_definition = soup.find("div", {"class": "otd-item-headword__pos"})
        definition = word_of_the_day_definition.text.strip().replace('\n', ' ')
        definition = definition.replace('   ', ': ', 1)
        definition = definition.replace('verb', 'Verb')
        definition = definition.replace('adjective', 'Adjective')
        definition = definition.replace('adverb', 'Adverb')
        definition = definition.replace('noun', 'Noun')
        definition = definition.replace('pronoun', 'Pronoun')
        definition = definition.replace('preposition', 'Preposition')
        
        daily = [
        f"""Subject:Word of the day: {wotd}\n\n{definition}""",

        f"""Subject:Archive""",

        f"""Subject:Languages"""
        ]

        np.save("./numpyemails/daily.npy", daily)

        with smtplib.SMTP(smtp, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                emails = np.load("/home/x/Desktop/documents/bin/AM/v6/numpyemails/daily.npy")
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
                emails = np.load("/home/x/Desktop/documents/bin/AM/v6/numpyemails/weekly.npy") #loading emails
                for idx, i in enumerate(emails): #idx fetches the index of workout.npy using enumerate
                        if idx != weekday: #if the index does not = the current day, skip it
                                continue
                        server.sendmail(sender_email, receiver_email, i) #sends the correct email
                        if idx == weekday: #if the index does = the current day, stop
                                break
                print(f"LOG: Weekly email sent at {logtime}")

schedule.every().day.at("06:00").do(Daily)
schedule.every().day.at("06:00").do(Weekly)
Startup()

while True:
    schedule.run_pending()
    time.sleep(1)
