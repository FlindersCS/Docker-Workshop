from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    name = "Tingkeng"
    fang = "wang2907"
    return f"Hello, {name} {fang}! - {os.environ['ENV_1']} - {os.environ['ENV_2']} - {os.environ['ENV_3']} - {os.environ['ENV_4']}"
