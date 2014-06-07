import logging

from flask import Flask

import config


app = Flask(__name__)

app.config.from_object('config')

from app import views
from app import api

logging.basicConfig(filename=config.LOGFILE,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

