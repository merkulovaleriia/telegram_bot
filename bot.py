from telegram.ext import Updater, CommandHandler

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('871029123:AAERML8MxToRXD_zVAbe5Ek2yzYrI-bcmTI')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()