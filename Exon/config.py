"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

import json
import os


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "23496202"
    API_HASH = "a1f882ad44ee621df511e060ef4ec719"
    APP_ID = "12410871"  # 2nd API_ID
    APP_HASH = "f7a7de22f129870e74bd87e9ef5320bd"  # 2ns API_HASH
    ARQ_API_KEY = "QBWGHT-LYRDZX-OVEHBS-MEKHOS-ARQ"
    BOT_ID = "5420854132"
    TOKEN = "5420854132:AAGYd_CytfcOjenkwsk4DhOUSotMmTiQ62k"
    OWNER_ID = "5399623240"
    OPENWEATHERMAP_ID = ""
    OWNER_USERNAME = "BerlinXbaap"
    BOT_USERNAME = "Draken_Xbot"
    SUPPORT_CHAT = "Mysticbots_Support"
    UPDATES_CHANNEL = "MysticXnetwork"
    SUPPORT_CHANNEL = "MysticXnetwork"
    JOIN_LOGGER = "-1001820696533"
    EVENT_LOGS = "-1001820696533"
    ERROR_LOGS = "-1001820696533"

    SQLALCHEMY_DATABASE_URI = "postgres://pkkarkxq:RWXrnL_Ggk5lBfnukigJRNDMn88I_tht@peanut.db.elephantsql.com/pkkarkxq"
    DB_URL = "postgres://pkkarkxq:RWXrnL_Ggk5lBfnukigJRNDMn88I_tht@peanut.db.elephantsql.com/pkkarkxq"
    MONGO_DB_URL = "mongodb+srv://TaktAsahina99:TaktAsahina99@cluster0.iq3cx2j.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = "mongodb+srv://TaktAsahina99:TaktAsahina99@cluster0.iq3cx2j.mongodb.net/?retryWrites=true&w=majority"
    DB_URL2 = "mongodb+srv://AranXD99:AranXD99@cluster0.ueowiiw.mongodb.net/?retryWrites=true&w=majority"  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.in"
    BOT_API_URL = "https://api.telegram.org/Draken_Xbot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "6KpHDWB1b~InSrl2UNOV3RZzPHpGEKkYva2DM1l8TB5w8y3Prdc2VPNCHxNHGvHF"
    SPAMWATCH_SUPPORT_CHAT = "@AnimeChatMystic"

    REDIS_URL = "redis://Draken99:Draken@99@redis-15058.c8.us-east-1-2.ec2.cloud.redislabs.com:15058/Rajni-free-db"

    DRAGONS = get_user_list("elevated_users.json", "1258798381 5519555383")
    DEV_USERS = get_user_list("elevated_users.json", "5387697107")
    REQUESTER = get_user_list("elevated_users.json", "")
    DEMONS = get_user_list("elevated_users.json", "1977550069 5526776892")
    INSPECTOR = get_user_list("elevated_users.json", "")
    TIGERS = get_user_list("elevated_users.json", "")
    WOLVES = get_user_list("elevated_users.json", "")

    DONATION_LINK = "https://t.me/Abishnoi1M"
    CERT_PATH = None
    STRICT_GBAN = "True"
    PORT = ""
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8
    BAN_STICKER = ""
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = "7058IAVQKYTP"
    WALL_API = ""
    AI_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    SPAMWATCH_API = "6KpHDWB1b~InSrl2UNOV3RZzPHpGEKkYva2DM1l8TB5w8y3Prdc2VPNCHxNHGvHF"
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "LSdLgCceYz8vNqFgJVzrkDgR"
    LASTFM_API_KEY = "FMLODA"
    CF_API_KEY = "KISS"
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "EXON"
    PHOTO = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    HELP_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    START_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    TIME_API_KEY = "5LB4TAKPEKZ0"
    INFOPIC = False
    GENIUS_API_TOKEN = "28jwoKAkskaSjsnsksAjnwjUJwj"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
