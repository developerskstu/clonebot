#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6218657811:AAGn5M1OPzIy4YCDaKu_jZtfaBIPgqtUnjw")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "22396233"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "e5cbafdf36380b9aff2f1f564dbd53c2")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQB5ouVz9PxYbszcCzxdaKU6lkDO8w8koIvwBpALMChNt34Qr1HnuKE0UXaQnFbzXd3g7WaLJM61B3gTfr48PaJD8Goe8Arxq9iR0AW_wzSvp_WGyOlUg2kkptfID_WCwPUVBLSlEKkyzJNv3Qf21YwcRndJ2m9oj91OOi2VB7Sz2Kgp6cyYV6CS4r20oMhliEyNC48UYcrNtfx5SwF0wKI5K_652P1e_G6ih_DM0BJHYqEUSirFmsPCBbtaapl8ClFGXBpOnkk6TZiZ1cIWEEPM7gpiX7QUofIczXKxjrbYM43LWzAFsBt1REXzZB4LEmL_DOpM2hJ4inuzxKAGM1cFAAAAAUAdQ2UA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://skrillex:<skrillex>@cluster0.qxyv732.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
