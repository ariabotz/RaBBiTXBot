import os
from os import getenv

""" Here is all variables we need for deploy userbot"""

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "25927541")) # API_ID get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "755b0d5e86f5469696fdd1abd0013c69") # API_HASH get it from my.telegram.org

# SESSIONS ~ Telegram 
SESSION = os.getenv("SESSION", "BQGLn3UAJOpgIQJqi5bUxPXwhLHfdrz_7m862YzeGibTOlE18tC8GXwIHc8gIqjARsv5kku78AyOVEwhhB9YOK9XkF1-8uvw9HqK22sb0EZZu4qs1A5hhfuxDZziJyRTSACAxgMB8In-cdEgbDPQx32B5OHzNzG1j7JrMoklb2iPQVw2cpDEa3LWxicxfQIZ964k2Z97C4I8wZc8cncr4dHAVIsI6Yi-nYotLjCLVI_9UBe-cX4tPwu_Hih878C3dDSpuUICB7pFxgfLFSUHyvGgTucOP2y2Sj07f53mQzd_Gi_I1qWjhLNGjMqlTSV1IBj9f4pXTGnRv7ZMaxjfoomV6zj6LgAAAAGQvnoQAA") # SESSION get it by @RaBBiTSessionBot on Telegram 
TOKEN = os.getenv("TOKEN", "6954728463:AAHebsmzoUZV2EROpxabM9r7nHJX1Y1IuxA") # BOT_TOKEN get it by @BotFather on Telegram 
LOGGER_ID = int(getenv("LOGGER_ID", "4152241957")) # LOGGER_ID fill here your logs telegram group id

# HANDLER ~ Telegram 
HANDLER = os.getenv("HANDLER", ".") # HANDLER fill here your command trigger

# DATABASES ~ mongodb.com
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ariaputrapratamaaaa:Helenasyg3cluster0.kk0whcj.mongodb.net/") # MONGO_URI fill here mongodb database url get it by mongodb.com

# PORN ~ spam
ALLOW_PORN = getenv("ALLOW_PORN", True) # u can enable and disable porn spam from here 

""" © @Imshivaexe """
#-----------------------------------------------------------------------------------------
""" You don't need to edit beyond this. """

ALIVE_PIC = os.getenv("ALIVE_PIC", "")
if not ALIVE_PIC:
    ALIVE_PIC = "https://graph.org/file/cbe8e398c5d84587b7a34.jpg"
    
HELP_PIC = os.getenv("HELP_PIC", "")
if not HELP_PIC:
    HELP_PIC = "https://graph.org/file/cbe8e398c5d84587b7a34.jpg"

PM_PIC = os.getenv("PM_PIC", "")
if not PM_PIC:
    PM_PIC = "https://graph.org/file/ddaac37448e7d58602ae6.jpg"

NEWS_API = os.getenv("NEWS_API", "")
if not NEWS_API:
    NEWS_API = "140dd16908d54879b350d0c7378306a5"

WEATHER_API = os.getenv("WEATHER_API", "")
if not WEATHER_API:
    WEATHER_API = "fadd97c7821d568d82f1cceaa06c7def"
    
BLACKLIST_CHAT = [
    -1002084534383,
]

BIO = getenv("BIO", "")
if not BIO:
    BIO = "〆 AriaBotz × XnXX.CoM 〆"
