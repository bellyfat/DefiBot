import json
import logging
import requests
from constant import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def load_abi(file_name):
    with open(f"./abi/{file_name}", "r") as f:
        return json.load(f)


def send_telegram_notice(msg):
    if not TELEGRAM_TOKEN:
        raise Exception("telegram token is null!")
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={msg}")
    logging.info("发送电报机器人提醒")
