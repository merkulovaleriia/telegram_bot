from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('871029123:AAERML8MxToRXD_zVAbe5Ek2yzYrI-bcmTI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()