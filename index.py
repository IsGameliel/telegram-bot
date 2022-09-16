from telegram import *
from telegram.ext import *


# My bot API token 
bot = Bot("input your own api-key")
print(bot.get_me()) 

updater=Updater("input your own api-key",use_context=True)
#use_context is use for if your telegram version is low than use false else use true

dispatcher=updater.dispatcher

def first_func(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to simvic.xyz where coding is made simple",
        )

start_process=CommandHandler('start', first_func)
dispatcher.add_handler (start_process)

# rule center 
def rules_func(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text = """
            Rules:
            Hi this channel is for educational purpose, violation of this rules will lead to a final ban
        """,
    )

start_process=CommandHandler('rules', rules_func)
dispatcher.add_handler(start_process)


#adding more Command
def second_func(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link: https://simvic.xyz/2022/08/27/python/ ",
        )

start_process=CommandHandler('python', second_func)
dispatcher.add_handler (start_process)

updater.start_polling()