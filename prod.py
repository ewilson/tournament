#uwsgi --socket 127.0.0.1:4242 --chdir /home/eric/tournament --module prod --callab app
from app import app

if __name__ == '__main__':
    app.run()
