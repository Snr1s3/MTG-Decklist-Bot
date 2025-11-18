from telegram import Update
from telegram.ext import ContextTypes

DEFAULT_MOXFIELD_USER = "Not found"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    moxfield_user = context.chat_data.get("moxfield_user", DEFAULT_MOXFIELD_USER)
    welcome_message =f"Hi, I'm MTG:Snrise!\nHow can I assist you today?\nUser: {moxfield_user}"
    print(context.args)
    await update.message.reply_text(welcome_message)