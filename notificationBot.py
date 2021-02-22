import yaml
import requests
import telebot
from bs4 import BeautifulSoup
from yaml.loader import FullLoader


# Getting telegram token
with open("config.yaml", 'r') as file:
    data = yaml.load(file, Loader=FullLoader)
    TELEBOT_TOKEN = data["TELEBOT_TOKEN"]
    TELEGRAM_GROUP = data["TELEGRAM_GROUP"]

# Configuring Telebot
bot = telebot.TeleBot(TELEBOT_TOKEN)
bot.config["api_key"] = TELEBOT_TOKEN


class NotificationBot():

    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.cookies = None
        self.headers = None
        self.data = None

        with open("itemlist.txt", 'r') as file:
            self.currentitems = set([line.strip() for line in file])

    def addHeaders(self, **kwrgs):
        if "cookies" in kwrgs.keys():
            self.cookies = kwrgs["cookies"]
        if "headers" in kwrgs.keys():
            self.headers = kwrgs["headers"]
        if "data" in kwrgs.keys():
            self.data = kwrgs["data"]

    def makeRequest(self, url, post=False):
        if not post:
            response = requests.get(
                url, headers=self.headers, cookies=self.cookies, data=self.data)
        else:
            response = requests.post(
                url, headers=self.headers, cookies=self.cookies, data=self.data)
        return response.text

    def send_notification(self, message):
        bot.send_message(TELEGRAM_GROUP, message)
