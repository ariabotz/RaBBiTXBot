import os
from os import getenv

""" Here is all variables we need for deploy userbot"""

# API_IDS ~ my.telegram.org
API_ID = int(getenv("API_ID", "25927541")) # API_ID get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "755b0d5e86f5469696fdd1abd0013c69") # API_HASH get it from my.telegram.org

# SESSIONS ~ Telegram 
SESSION = os.getenv("SESSION", "1BVtsOGcBuxyLole1-SRZsV00tuyFrC9EN1gp789RWgghrcg2kHbWJTKbEjW7e9zM5nQJL3LLihdJsZRPWWDNMITD031EsM4ilvIMn1tV3BnmEUoMVZLbSbPzfNRCqo5ToKd1FwkwIO1rU1IqO24uePE74dNQV1hNsqPZQg-af_k6Nrm7jDiDVh92cL33dHIq4pJMQoaUQlgWpDsCD_NIe_DFW1qSXciKr6w59oWkZ773AdW9eSOcvnEfCsfnTlDd3r7n6U_uKuVSQXuOsB33hlWNw56OmghoccPhpNmS8v0OLYMFIGfwtnG7WGT1uVn-mKYEbZvWumvpqye7CiAyUgamppq79D4=") # SESSION get it by @RaBBiTSessionBot on Telegram 
TOKEN = os.getenv("TOKEN", "6954728463:AAHebsmzoUZV2EROpxabM9r7nHJX1Y1IuxA") # BOT_TOKEN get it by @BotFather on Telegram 
LOGGER_ID = int(getenv("LOGGER_ID", "")) # LOGGER_ID fill here your logs telegram group id

# HANDLER ~ Telegram 
HANDLER = os.getenv("HANDLER", ".") # HANDLER fill here your command trigger

# DATABASES ~ mongodb.com
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ariaputrapratamaaa:<password>@cluster0.lksiqox.mongodb.net/") # MONGO_URI fill here mongodb database url get it by mongodb.com

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
