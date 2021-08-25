# from https://realpython.com/flask-by-example-part-1-project-setup/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"