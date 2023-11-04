import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    Application,
)
import os
import dotenv
import interpreter
import openai

# get current PID
pid = os.getpid()
# prevent from sleeping until this script is finished
os.system(f"caffeinate -w {pid} &")

dotenv.load_dotenv()

FILE_SEND_ACTION = "SendFile: "

interpreter.model = "gpt-4"
interpreter.auto_run = True
interpreter.system_message += """
If the user wants you send them a file, add the following line to your response:

SendFile: <file_path>
"""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def send_file(file_path: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            await context.bot.send_document(
                chat_id=update.message.chat_id, document=file
            )
    else:
        await update.message.reply_text("Sorry, the file does not exist.")


async def free_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = interpreter.chat(update.message.text)
    interpreter.messages = messages
    assistant_response = messages[-1]["message"]

    if FILE_SEND_ACTION in assistant_response:
        file_path = assistant_response.split(FILE_SEND_ACTION)[1].split("\n")[0]
        await send_file(file_path, update, context)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=assistant_response
        )


async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    interpreter.messages = []
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="History cleared."
    )

async def post_init(application: Application) -> None:
    await application.bot.set_my_commands(
        [
            ("start", "Start the bot"),
            ("clear", "Clear the chat history"),
        ]
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).post_init(post_init).build()

    start_handler = CommandHandler("start", start)
    clear_history_handler = CommandHandler(
        "clear", clear_history, filters=filters.User(username="@balesni")
    )
    free_text_handler = MessageHandler(
        filters.TEXT & filters.User(username="@balesni"), free_text
    )

    application.add_handler(start_handler)
    application.add_handler(clear_history_handler)
    application.add_handler(free_text_handler)

    application.run_polling()
