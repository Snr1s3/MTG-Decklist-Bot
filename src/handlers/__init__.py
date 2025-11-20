from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters

from .get_decks import start_list
from .start import start
from .get_decks import LOCATION, start_list, return_decklist
from .set_user import set_user
from .send_pdf import send_pdf
from .decklist import (
    ASK_DECK_NAME,
    ASK_DECKLIST,
    start_savedeck,
    receive_deck_name,
    receive_decklist,
    cancel,
)


def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setuser", set_user))
    app.add_handler(CommandHandler("sendpdf", send_pdf))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("savedeck", start_savedeck)],
        states={
            ASK_DECK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_deck_name)],
            ASK_DECKLIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_decklist)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("list", start_list)],
        states={
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, return_decklist)],
            },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)