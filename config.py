import os

ROOT = os.path.dirname(__file__)
DATABASE = ROOT + '/data/tourn.db'
SCHEMA = ROOT + '/data/schema.sql'
TEST_DATABASE = ROOT + '/data/tourn_test.db'
LOGFILE = ROOT + '/log/tournament.log'
CSRF_ENABLED = True
SECRET_KEY = 'super-secure-open-source-project'
PASSWORD = 'ping-pong'
