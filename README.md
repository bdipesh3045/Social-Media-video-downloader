Short video Downloader from platforms Insta, Meta and Tiktok
# 📘 Telegram Bot for Downloading Shorts

Easily download all your shorts using a simple telegram bot. It uses unofficial api from two sites like [sstk](https://ssstik.io) and [fastdl](https://fastdl.app/) and FB scrapper to get downloadable link. This bot can be deployed to any serverless hosting provider as it uses flask , gunicorn and most importantly iobytes to perform all its tasks

## 🔍 Problem Statement
Tired of manually going to different sites to download video just simply use this BOT and your videos will stay forever in the telegram no need to worry that video will be removed.

## 💡 Solution
Utilize the  sstk and fastdl website api which can be found using network inspect and then copy that and goi to [curlconverter](https://curlconverter.io) 


## 🚀 Key Features
- All different platform videos will be grouped together in different subchannels.
- Seamless conversion of web content into eBooks.
- Can be easily deployed on free platform [render](https://.render.com) 

## 🛠️ Technical Details
- Deployed using Flask framework.
- Used IOBYTES to perform all data download and transfer.
- Created flask webhook to handle response.
- Secure authentication using environment variables.


## Demo
![ezgif-6-670c2fe48f (1)](https://github.com/bdipesh3045/Social-Media-video-downloader/assets/111185281/bdb8417a-ad59-4d10-a98d-43b2aab857f9)


## Obtaining the api
To obtain the unofficial api for downloading tiktok watch this video [Youtube](https://youtu.be/UsT11sOD1JA?t=699) from 11:33 to 14:40 and can do similar for facebook from site sstk.



# Environment Variables

This project utilizes environment variables for configuration. Below are the variables used and their purposes:

- `fb`: Sub group/topic ID for meta related to Facebook.
- `ID`: Main chat ID.
- `tiktok`: Sub group/topic ID for meta related to TikTok.
- `ig`: Sub group/topic ID for meta related to Instagram.
- `tg`: Telegram bot token.

Ensure to set these variables according to your requirements before running the project.

## Installation & Deployment

Install this project using the command below:

 ```bash
 git clone https://github.com/rsgalloway/instapaper.git
 cd instapaper
 python setup.py install
```

```bash
pip install -r requirements.txt

```
For deployment we will be using Gunicorn and setting out the time out to 600 so we can perform all tasks.

```bash
gunicorn --timeout 240 app:app

```

## 🌟 Conclusion
A fun and challenging project that involved properly download videos from different platform and properly deploying it in a free tier plan so it can run forever.



## Support

For support, message me on linkedin : [Dipesh Sharma](https://www.linkedin.com/in/dipesh-sharma-b04948202/).


Email Address: dipeshsharma9800@gmail.com

## 📚 This repository is for educational purposes only; it does not intend to damage property.
