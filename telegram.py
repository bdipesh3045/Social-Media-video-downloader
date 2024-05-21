import csv
import pandas as pd
import threading
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from main import download_tiktok, insta_reel, fbreel
import io

load_dotenv()
import os

base_url = f"""https://api.telegram.org/bot{os.getenv("tg")}"""

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


def main_msg(link_social):
    fb = os.getenv("fb")
    ID = os.getenv("ID")
    tiktok = os.getenv("tiktok")
    ig = os.getenv("ig")
    # this is for tiktok
    parameter_error = {
        "chat_id": ID,
        "text": "You have done some mistake while sending the url.",
    }
    video = True

    if "tiktok" in link_social:

        parameter_tiktok = {
            "chat_id": ID,
            "message_thread_id": tiktok,
        }
        video, filename = download_tiktok(link=link_social)
    elif "instagram" in link_social:
        parameter_tiktok = {
            "chat_id": ID,
            "message_thread_id": ig,
        }
        video, filename = insta_reel(link=link_social)

    elif "facebook" in link_social:
        parameter_tiktok = {
            "chat_id": ID,
            "message_thread_id": fb,
        }
        video, filename = fbreel(link=link_social)
    else:
        video = False
    if video:
        files = {"video": (filename, io.BytesIO(video), "video/mp4")}
        resp = requests.get(base_url + "/sendVideo", data=parameter_tiktok, files=files)
        print(resp.text)
    else:
        resp = requests.get(base_url + "/sendMessage", data=parameter_error)
        print(resp.text)


while True:
    print("Waiting for messages.....")
    got = update()

    checker = got["message_id"]
    if initial != checker:
        initial = checker
        main_msg(got["text"])
        print(got["text"])
    time.sleep(1)
