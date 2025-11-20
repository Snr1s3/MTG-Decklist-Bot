from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
import re

from ..utils.crud_mongo import MongoCRUD

ASK_DECK_NAME, ASK_DECKLIST = range(2)
async def start_savedeck(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Please send the deck name:")
    return ASK_DECK_NAME

async def receive_deck_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["deck_name"] = update.message.text
    await update.message.reply_text("Now send the decklist (as text):")
    return ASK_DECKLIST

async def receive_decklist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    deck_name = context.user_data.get("deck_name", "Unnamed Deck")
    msg = update.message.text.split()
    print(f"\n{context}\n\n\n")
    convert = []
    st = ""
    msg = [m for m in msg if m != '*F*']
    print(msg)
    for idx, m in enumerate(msg):
        if idx == 0:
            st += m
        else:
            anterior = msg[idx-1]
            anterior_num = re.sub(r'[^\d()]', '', anterior)  
            if anterior_num.isdigit() and m.isdigit():
                convert.append(st)
                st = "" 
            st += f" {m}"
        if idx == len(msg) - 1:
            convert.append(st)
    mongo = MongoCRUD()
    mongo.create(deck_name,convert)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Deck save cancelled.")
    return ConversationHandler.END