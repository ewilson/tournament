from flask import Flask
from flask_bootstrap import Bootstrap
import logging
import config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')

from app import views

logging.basicConfig(filename=config.LOGFILE,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')

