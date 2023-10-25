from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    name = "Alex Crush"
    fan = "crus0018"
    return f"Hello, {name}! FAN: {fan} - {os.environ['ENV_1']}, {os.environ['ENV_2']}, {os.environ['ENV_3']}, {os.environ['ENV_4']} "
