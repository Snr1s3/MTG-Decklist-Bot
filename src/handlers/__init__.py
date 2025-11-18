from telegram.ext import CommandHandler
from .start import start
from .set_user import set_user
from .send_pdf import send_pdf


def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setuser", set_user))
    app.add_handler(CommandHandler("sendpdf", send_pdf))