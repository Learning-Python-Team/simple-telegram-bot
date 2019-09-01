from functools import wraps
from . import log
import emoji
import traceback
import telegram


def send_typing_action(func):
    """Sends typing action while processing func command."""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)        
        return func(update, context,  *args, **kwargs)
    return command_func


def get_chat_id(update):    
    return update.effective_message.chat_id 

def send_system_message(bot, subject, plainTextMessage=None,  send_to_bot=True):
    if send_to_bot:
        send_bot_message(bot, app.config['ADMIN_CHAT_ID'], emoji.emojize(" :exclamation: {}".format(subject)))
    log.info("{} \t {}".format(subject, plainTextMessage))
