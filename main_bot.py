from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import math

def start(bot, update):
    update.message.reply_text('Hey, {}, you are welcome to this cozy bot!'.format(update.message.from_user.first_name))

def hello(bot, update):
    update.message.reply_text(
        'Hello, {}, do you wanna have some fun with math? \n\nAlso check this out our new /bop feature'.format(update.message.from_user.first_name))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def calc(bot, update):
    exp = update.message.text.replace('/calc', '')
    exp = "".join(exp.split())
    if re.match('^([-+]?([(]?[0-9][)]?[+-/*]?))*$', exp):
        try:
            update.message.reply_text(eval(exp))
        except:
            update.message.reply_text('Error calculating')
    else:
        update.message.reply_text('Wrong pattern')

def add(bot, update):
    param = update.message.text.replace('/add', '').split()
    result = int(param[0])+int(param[1])
    update.message.reply_text("Result: {}".format(result))

def substitute(bot, update):
    param = update.message.text.replace('/substitute', '').split()
    result = int(param[0])-int(param[1])
    update.message.reply_text("Result: {}".format(result))

def divide(bot, update):
    param = update.message.text.replace('/divide', '').split()
    result = int(param[0])/int(param[1])
    update.message.reply_text("Result: {}".format(int(result)))

def multiply(bot, update):
    param = update.message.text.replace('/multiply', '').split()
    result = int(param[0])*int(param[1])
    update.message.reply_text("Result: {}".format(result))

def help(bot, update):
    update.message.reply_text('Check this out our bot options: \n /start \n /hello \n /bop')
    
def main():
    updater = Updater('871029123:AAERML8MxToRXD_zVAbe5Ek2yzYrI-bcmTI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('hello',hello))
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('calc',calc))
    dp.add_handler(CommandHandler('add',add))
    dp.add_handler(CommandHandler('substitute',substitute))
    dp.add_handler(CommandHandler('divide',divide))
    dp.add_handler(CommandHandler('multiply',multiply))
    dp.add_handler(CommandHandler('help',help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()