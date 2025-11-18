from telegram import Update
from telegram.ext import ContextTypes

async def send_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pdf_path = "output.pdf"  # Path to your PDF file
    await update.message.reply_document(document=open(pdf_path, "rb"))