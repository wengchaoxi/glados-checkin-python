# -*- coding: utf-8 -*-
# https://github.com/wengchaoxi/glados-checkin-python

import os
import time
import urllib.request
import urllib.parse
import json
import threading
import argparse
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("[WARN] dotenv not installed, try `pip install python-dotenv`")

__cookie = os.environ.get("GLADOS_COOKIE")
assert __cookie, "Require Env `GLADOS_COOKIE`!"
__webhook = os.environ.get("FEISHU_WEBHOOK", "")

def feishu(webhook, message):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "msg_type": "text",
        "content": {
            "text": "[GLADOS] " + message
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(webhook, data=data, headers=headers)
    response = urllib.request.urlopen(req)
    response_dict = json.loads(response.read().decode("utf-8"))
    message = response_dict["StatusMessage"]
    print("[INFO] Feishu Notify {}".format(message.upper()))

def checkin():
    url = "https://glados.rocks/api/user/checkin"
    headers = {
        "Cookie": __cookie,
        "Origin": "https://glados.rocks",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    payload = {
        "token": "glados.one"
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)
    response_dict = json.loads(response.read().decode("utf-8"))
    print("[INFO] Glados {}".format(response_dict["message"]))
    if __webhook != "":
        message = response_dict["message"]
        feishu(__webhook, message)

def schedule(interval):
    while True:
        time.sleep(interval)
        checkin()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interval", type=float, default=None, help="Checkin interval, in hours")
    args = parser.parse_args()
    interval = args.interval
    if interval is None:
        checkin()
    else:
        threading.Thread(target=schedule, args=(interval*3600,)).start()
