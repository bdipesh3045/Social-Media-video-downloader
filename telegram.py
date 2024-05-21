import csv
import pandas as pd
import threading
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()
import os

base_url = "https://api.telegram.org/bot"
url = f"""https://api.telegram.org/bot{os.getenv("tg")}/getUpdates"""


def update():
    resp = requests.get(url)
    data = resp.json()
    length = len(data["result"])
    # print(length)
    info = {}
    for p in data["result"][length - 1]["message"]:
        if p == "message_id" or p == "text":
            info[p] = data["result"][length - 1]["message"][p]
            # print(f"{p}:{data['result'][0]['message'][p]}")
        if p == "chat" or p == "from":
            for c in data["result"][length - 1]["message"][p]:
                # print(f"{c}:{data['result'][0]['message'][p][c]}")
                info[c] = data["result"][length - 1]["message"][p][c]
    return info


y = update()

initial = y["message_id"]


# Create a new thread and run the remove_files function in it

# thread = threading.Thread(target=counter)
# thread.start()
while True:
    print("Waiting for messages.....")
    got = update()

    checker = got["message_id"]
    if initial != checker:
        initial = checker
        print(got["text"])
    time.sleep(1)
