from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    FAN = "WICK0133"
    Name="zec"
    return f"Name: {Name}, Fan: {FAN} - {os.environ['ENV_1']}, {os.environ['ENV_2']}, {os.environ['ENV_3']}, {os.environ['ENV_4']}"
