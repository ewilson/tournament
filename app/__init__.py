from flask import Flask
from flask_bootstrap import Bootstrap
import logging

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')

from app import views

logging.basicConfig(filename='log/tournament.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')

