from flask import Flask
import os

app = Flask(__name__)


@app.route('/python/')
def hello_world():
    uid = os.geteuid()
    if(uid == 0):
        return "You have root permissions"
    else:
        return "You don't have root permissions. Your uid: " + str(uid)
