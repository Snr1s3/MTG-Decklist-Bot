from telegram import Update
from telegram.ext import ContextTypes
from ..utils.crud_mongo import MongoCRUD

LOCATION = range(1)
async def start_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Choose an option:\nLOCAL [1]\nMoxfield[2]\nCancel[3]")
    return LOCATION


async def return_decklist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    msg = update.message.text.strip()
    if msg == "1":
        mongo = MongoCRUD()
        decks = mongo.get_all_decks()
        if decks:
            reply = "\n".join(
                f"{deck['deck_name']} | Commander(s): {', '.join(deck['commander'])}\n"
                for deck in decks
            )
            await update.message.reply_text(reply)
        else:
            await update.message.reply_text("No decks found.")
    else:
        await update.message.reply_text("Wrong option")