from telegram.ext import Updater, PrefixHandler, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import telegram
from ext.utils import print_error
from config import Config 
def main():
    print_error("running...")
    print(Config.BOT_API_KEY)

if __name__ == '__main__':
    main()
