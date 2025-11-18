# This file is used to initialize the config package. It may contain configuration settings such as the bot token and other constants.
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment.")
API_URL = "https://api.telegram.org/bot" + BOT_TOKEN + "/"
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"


