import requests
import re
import json
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import io
import uuid


# Function to extract text from JSON string
def clean_str(s):
    return json.loads('{"text": "' + s + '"}')["text"]


# Function to extract download link from content based on regex pattern
def get_link(content, pattern):
    match = re.search(pattern, content)
    if match:
        return clean_str(match.group(1))
    return None


# Function to extract video ID from URL
def generate_id(url):
    if url.isdigit():
        return url
    match = re.search(r"\/(?:t\.\d+\/)?(\d+)", url)
    if match:
        return match.group(1)
    return ""


# Function to extract video title from content
def get_title(content):
    match = re.search(
        r'<title>(.*?)<\/title>|title id="pageTitle">(.+?)<\/title>', content
    )
    if match:
        return match.group(1) or match.group(2)
    return None


# Function to download Facebook reel video given its URL
def download_facebook_reel(video_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "Authority": "www.facebook.com",
        "Sec-Ch-Ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
    }
    try:
        response = requests.get(video_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "message": str(e)}

    msg = {"ok": True}
    msg["id"] = generate_id(video_url)
    msg["title"] = clean_str(get_title(response.text))
    sd_link = get_link(response.text, r'browser_native_sd_url":"([^"]+)"')
    if sd_link:
        msg.setdefault("links", {})["sd_quality"] = sd_link + "&dl=1"
    hd_link = get_link(response.text, r'browser_native_hd_url":"([^"]+)"')
    if hd_link:
        msg.setdefault("links", {})["hd_quality"] = hd_link + "&dl=1"
    return msg


# Insta
def fbreel(link):
    result = download_facebook_reel(link)
    link = result.get("links")

    if link.get("hd_quality"):
        down = link.get("hd_quality")
    else:
        down = link.get("sd_quality")
    filename = f"""{result.get("id")}.mp4"""

    mp4File = urlopen(down)
    # Feel free to change the download directory

    video_data = io.BytesIO()

    while True:
        data = mp4File.read(4096)
        if data:
            video_data.write(data)
        else:
            break

    video_data.seek(0)  # Rewind the BytesIO object to the beginning

    return (video_data.getvalue(), filename)


def insta_reel(link):
    unique_id = uuid.uuid4()

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://fastdl.app",
        "Referer": "https://fastdl.app/en",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    json_data = {
        "url": link,
        "ts": 1716280023993,
        "_ts": 1716211953367,
        "_tsc": 4823488,
        "_s": "42f23d0164b9af7e9dd682f36b1f5099afa87caa0a1693fca5f3c54f8b171714",
    }

    response = requests.post(
        "https://fastdl.app/api/convert", headers=headers, json=json_data
    )

    main_link = dict(response.json())

    down_link = main_link["url"][0]["url"]

    mp4File = urlopen(down_link)
    # Feel free to change the download directory

    video_data = io.BytesIO()

    while True:
        data = mp4File.read(4096)
        if data:
            video_data.write(data)
        else:
            break

    video_data.seek(0)  # Rewind the BytesIO object to the beginning

    # Send the video
    video_filename = f"{unique_id}.mp4"
    return (video_data.getvalue(), video_filename)


def download_tiktok(link):

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "HX-Current-URL": "https://ssstik.io/how-to-download-tiktok-video",
        "HX-Request": "true",
        "HX-Target": "target",
        "HX-Trigger": "_gcaptcha_pt",
        "Origin": "https://ssstik.io",
        "Referer": "https://ssstik.io/how-to-download-tiktok-video",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    params = {
        "url": "dl",
    }

    data = {
        "id": link,
        "locale": "en",
        "tt": "bktkQm1j",
    }

    response = requests.post(
        "https://ssstik.io/abc", params=params, headers=headers, data=data
    )

    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    data = link.split("/")
    video_id = data[data.index("video") + 1]

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory

    video_data = io.BytesIO()

    while True:
        data = mp4File.read(4096)
        if data:
            video_data.write(data)
        else:
            break

    video_data.seek(0)  # Rewind the BytesIO object to the beginning

    video_filename = f"{video_id}.mp4"
    return (video_data.getvalue(), video_filename)
