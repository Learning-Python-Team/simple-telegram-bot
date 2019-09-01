import sys
import os
from dotenv import load_dotenv
from os.path import join, dirname
from ext.utils import print_error

settings_file = 'production.env'

if not os.path.exists(settings_file):
    print_error("Could not find file {} so exiting!".format(settings_file))
    sys.exit(1)


dotenv_path = join(dirname(__file__), 'production.env')

load_dotenv(dotenv_path, verbose=True)


class Config(object):      
    BOT_API_KEY = os.getenv('BOT_API_KEY')
    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False

