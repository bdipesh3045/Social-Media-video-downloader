from flask import Flask, request

import requests
from dotenv import load_dotenv
from main import download_tiktok, insta_reel, fbreel
import io

load_dotenv()
import os

base_url = f"""https://api.telegram.org/bot{os.getenv("tg")}"""

url = f"""https://api.telegram.org/bot{os.getenv("tg")}/getUpdates"""

app = Flask(__name__)

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


@app.route("/setwebhook", methods=["GET", "POST"])
def hook():

    if request.method == "POST":
        try:
            # Handle POST request

            data = request.data
            data_dict = json.loads(data.decode("utf-8"))

            value = data_dict["message"]["text"]
            main_msg(value)
   
            return "Done"
        except Exception as e:
            # SO that the function gives the telegram webhook response 200 otherwise it will tray again and dont allow other messages to be processes which will freeze the system
            return "Done"
    return "This is a GET request"


@app.route("/")
def home():
    return "Hello. I am working"


