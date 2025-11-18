from telegram import Update
from telegram.ext import ContextTypes

async def set_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /setuser <moxfield user>")
        return
    new_user = " ".join(context.args).strip()
    if len(new_user) > 40:
        await update.message.reply_text("user too long.")
        return
    context.chat_data["moxfield_user"] = new_user
    await update.message.reply_text(f"Saved user for this chat: {new_user}")